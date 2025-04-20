from PySide6 import QtCore, QtWidgets, QtGui
from thefuzz import fuzz
from PySide6.QtCore import Qt
from utils.get_apps import get_apps
from utils.launch_app import launch_app


cached_apps = []
for app in get_apps():  # type: ignore
    cached_apps.append(app)


def fuzzy_partial_match(query, choices, limit=3):
    scored = [
        (choice, fuzz.partial_token_sort_ratio(query, choice)) for choice in choices
    ]
    return sorted(scored, key=lambda x: x[1], reverse=True)[:limit]


class MainWindow(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        # initial window stuff
        self.setFixedSize(700, 100)
        self.setWindowTitle("Starlit")
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)

        # layout and entry stuff
        self.layout = QtWidgets.QVBoxLayout(self)
        self.entry = QtWidgets.QLineEdit()
        self.entry.setPlaceholderText("")
        self.entry.setFixedSize(700, 100)
        self.entry.textChanged.connect(self.finder)

        # define theme
        with open("style/style.qss", "r") as f:
            self.setStyleSheet(f.read())

        self.layout.setContentsMargins(0, 0, 0, 0)
        self.layout.addWidget(self.entry)

    # equivalent to escclose()
    def keyPressEvent(self, event: QtGui.QKeyEvent):
        if event.key() == Qt.Key_Escape:
            self.close()
        elif event.key() == Qt.Key_Return:
            self.handle_open_app()

    def finder(self):
        print(self.entry.text())

        filtered_apps = []
        if len(self.entry.text()) > 1:
            filtered_apps = [
                match[0].getName()
                for match in fuzzy_partial_match(self.entry.text(), cached_apps)
            ]
        return filtered_apps

    def handle_open_app(self):
        apps = cached_apps
        app_name = self.finder()
        for app in apps:
            if len(app_name) != 0 and app.getName().lower() == app_name[2].lower():
                launch_app(app.getExec())
                self.close()

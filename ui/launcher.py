from PySide6 import QtCore, QtWidgets, QtGui
from thefuzz import fuzz
from PySide6.QtCore import Qt
from utils.get_apps import get_apps
from utils.launch_app import launch_app
from ui.simpleresult import SimpleResult

cached_apps = []
for app in get_apps():  # type: ignore
    cached_apps.append(app)


def fuzzy_partial_match(query, choices, limit=3, cut_off=70):
    scored = []
    for choice in choices:
        score = fuzz.partial_token_sort_ratio(query, choice)
        if score >= cut_off:
            scored.append((choice, score))
    return sorted(scored, key=lambda x: x[1], reverse=True)[:limit]


class MainWindow(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        # initial window stuff
        self.setFixedSize(700, 100)
        self.setWindowTitle("Starlit")
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setWindowFlag(QtCore.Qt.WindowStaysOnTopHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)

        # layout and entry stuff
        self.layout = QtWidgets.QVBoxLayout(self)
        self.entry = QtWidgets.QLineEdit()
        self.entry.setPlaceholderText("search away!")
        self.entry.setFixedSize(700, 100)
        self.entry.textChanged.connect(self.updater)

        # define theme
        with open("style/style.qss", "r") as f:
            self.setStyleSheet(f.read())

        self.layout.setContentsMargins(0, 0, 0, 0)
        self.layout.addWidget(self.entry)

    # equivalent to escclose()
    def keyPressEvent(self, event: QtGui.QKeyEvent):
        match event.key():
            case Qt.Key_Escape:
                self.close()
            case Qt.Key_Return:
                self.handle_open_app()

    def finder(self):
        if len(self.entry.text()) > 2:
            return [
                match[0]
                for match in fuzzy_partial_match(self.entry.text(), cached_apps)
            ]
        return []

    def updater(self):
        for i in reversed(range(1, self.layout.count())):
            item = self.layout.itemAt(i)
            widget = item.widget()
            if widget:
                widget.setParent(None)

        filtered_apps = self.finder()
        for app in filtered_apps[:2]:
            widget = SimpleResult(app.getName(), app.getIcon())
            self.layout.addWidget(widget)

        self.setFixedHeight(100 + (len(filtered_apps) * 100))

    def handle_open_app(self):
        app_name = self.finder()
        if app_name:
            launch_app(app_name[0].getExec())
            self.close()

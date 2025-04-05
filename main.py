import sys, random
from PySide6 import QtCore, QtWidgets, QtGui
from PySide6.QtCore import Qt
from utils.get_apps import get_apps
from utils.launch_app import launch_app

class MainWindow(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        # initial window stuff
        self.layout = QtWidgets.QVBoxLayout(self)
        self.entry = QtWidgets.QLineEdit()
        self.entry.setPlaceholderText("")
        self.entry.setFixedSize(700, 100)      
        self.entry.textChanged.connect(self.finder)

        # define theme
        with open('./style/style.qss', "r") as f:
            self.setStyleSheet(f.read())

        self.layout.setContentsMargins(0, 0, 0, 0)  
        self.layout.addWidget(self.entry)


    # equivalent to escclose()
    def keyPressEvent(self, event: QtGui.QKeyEvent):
        if event.key() == Qt.Key_Escape:
            appie.exit()
        elif event.key() == Qt.Key_Return:
            self.handle_open_app()
        
        
    def finder(self):
        print(self.entry.text())
        filtered_apps = [app.getName() for app in get_apps() if app.getName().lower().startswith(self.entry.text().lower())]
        return filtered_apps[:2]
    
    def handle_open_app(self):
        apps = get_apps()
        app_name = self.finder()
        for app in apps:
            if len(app_name) != 0 and app.getName().lower() == app_name[0].lower():
                launch_app(app.getExec())
                appie.exit()


if __name__ == "__main__":
    appie = QtWidgets.QApplication([])

    widget = MainWindow()
    widget.setFixedSize(700,100)
    widget.setWindowTitle("Starlit")
    widget.show()

    sys.exit(appie.exec())
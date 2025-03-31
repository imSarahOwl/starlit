import sys, random, utils.get_apps
from PySide6 import QtCore, QtWidgets, QtGui
from PySide6.QtCore import Qt
import utils.get_apps

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
            sys.exit(app.exec())
    def finder(self):
        print(self.entry.text())
        filtered_apps = [app.getName() for app in utils.get_apps.get_apps() if app.getName().lower().startswith(self.entry.text().lower())]
        for app in filtered_apps:
            print(app)


if __name__ == "__main__":
    app = QtWidgets.QApplication([])

    widget = MainWindow()
    widget.setFixedSize(700,100)
    widget.setWindowTitle("Starlit")
    widget.show()

    sys.exit(app.exec())
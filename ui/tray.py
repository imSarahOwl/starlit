from PySide6 import QtWidgets
from PySide6.QtGui import QIcon, QAction


class Tray:
    def __init__(self, app, new_window):
        # start to define the tray
        self.icon = QIcon("icon.png")
        self.tray = QtWidgets.QSystemTrayIcon()
        self.tray.setIcon(self.icon)
        self.tray.setToolTip("starlit!")

        # ok now we have a menu :p
        self.menu = QtWidgets.QMenu()
        self.open = QAction("open")
        self.open.triggered.connect(new_window)
        self.menu.addAction(self.open)

        self.quit = QAction("quit")
        self.quit.triggered.connect(app.quit)
        self.menu.addAction(self.quit)

        self.tray.setContextMenu(self.menu)
        self.tray.show()

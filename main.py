import sys
from PySide6 import QtWidgets
from PySide6.QtGui import QIcon, QAction

from ui.launcher import MainWindow


def new_window():
    w = MainWindow()
    w.show()
    open_windows.append(w)


# biggest gambiarra of my life (sim sou br :p)

open_windows = []

if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    app.setQuitOnLastWindowClosed(False)

    # start to define the tray
    icon = QIcon("icon.png")
    tray = QtWidgets.QSystemTrayIcon()
    tray.setIcon(icon)
    tray.setToolTip("starlit!")

    # ok now we have a menu :p
    menu = QtWidgets.QMenu()
    open = QAction("open")
    open.triggered.connect(new_window)
    menu.addAction(open)

    quit = QAction("quit")
    quit.triggered.connect(app.quit)
    menu.addAction(quit)

    tray.setContextMenu(menu)
    tray.show()
    sys.exit(app.exec())

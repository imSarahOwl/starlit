import sys
from PySide6 import QtCore, QtWidgets
from PySide6.QtNetwork import QLocalServer, QLocalSocket
from PySide6.QtGui import QIcon, QAction

from ui.launcher import MainWindow

APP_ID = "xyz.missowl.Starlit"


def another_running_instance():
    socket = QLocalSocket()
    socket.connectToServer(APP_ID)
    is_running = socket.waitForConnected(100)
    socket.abort()
    return is_running


def create_server():
    server = QLocalServer()
    server.removeServer(APP_ID)
    server.listen(APP_ID)
    return server


def new_window():
    w = MainWindow()
    w.show()
    open_windows.append(w)


# biggest gambiarra of my life (sim sou br :p)

open_windows = []

if __name__ == "__main__":
    if another_running_instance():
        print("it's already running >:p")
        sys.exit(0)

    app = QtWidgets.QApplication([])
    server = create_server()
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

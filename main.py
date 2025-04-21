import sys, argparse
from PySide6 import QtCore, QtWidgets
from PySide6.QtGui import QIcon, QAction
from utils.server import another_running_instance, create_server, send_message
from ui.launcher import MainWindow

APP_ID = "xyz.missowl.Starlit"

parser = argparse.ArgumentParser(
    description="A fast and extendable application launcher with plugin support"
)
parser.add_argument("--toggle", action="store_true", help="launch new starlit window")

args = parser.parse_args()


def on_new_connection():
    socket = server.nextPendingConnection()
    if socket and socket.waitForReadyRead(1000):
        message = socket.readAll().data().decode()
        match message:
            case "toggle":
                new_window()
            case _:
                print(message)
        socket.close()


def new_window():
    w = MainWindow()
    w.show()
    open_windows.append(w)


open_windows = []

if __name__ == "__main__":
    if args.toggle and another_running_instance():
        send_message("toggle")
        sys.exit(0)

    if another_running_instance():
        print("it's already running >:p")
        sys.exit(0)

    app = QtWidgets.QApplication([])
    server = create_server()
    server.newConnection.connect(on_new_connection)
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

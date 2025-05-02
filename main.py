import sys, argparse
from PySide6 import QtCore, QtWidgets
from utils.server import (
    another_running_instance,
    create_server,
    send_message,
    on_new_connection,
)
from ui.launcher import MainWindow
from ui.tray import Tray

APP_ID = "xyz.missowl.Starlit"

parser = argparse.ArgumentParser(
    description="A fast and extendable application launcher with plugin support"
)
parser.add_argument("--toggle", action="store_true", help="launch new starlit window")

args = parser.parse_args()


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
    app.setQuitOnLastWindowClosed(False)
    server = create_server()
    server.newConnection.connect(lambda: on_new_connection(server, new_window))

    tray = Tray(app, new_window)
    print("starlit is running!")
    sys.exit(app.exec())

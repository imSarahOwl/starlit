from PySide6.QtNetwork import QLocalServer, QLocalSocket
from PySide6.QtCore import QTimer

APP_ID = "xyz.missowl.Starlit"


def send_message(msg):
    if another_running_instance():
        socket = QLocalSocket()
        socket.connectToServer(APP_ID)
        socket.write(str.encode(msg))
        socket.flush()
        socket.disconnectFromServer()


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

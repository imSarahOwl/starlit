from PySide6 import QtWidgets, QtCore, QtGui


class SimpleResult(QtWidgets.QWidget):
    def __init__(self, name, icon):
        super().__init__()
        self.setFixedSize(700, 100)
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setWindowFlag(QtCore.Qt.WindowStaysOnTopHint)

        self.layout = QtWidgets.QHBoxLayout(self)
        self.svgicon = QtGui.QIcon(icon)
        self.svgicon.setFixedSize(48, 48)

        self.label = QtWidgets.QLabel(name)

        self.layout.addWidget(self.svgicon)
        self.layout.addWidget(self.label)
        self.layout.addStretch()

        self.setStyleSheet("""
            padding-left: 25px;
            font-size: 24px
        """)

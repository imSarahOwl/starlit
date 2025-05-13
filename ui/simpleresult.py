from PySide6 import QtWidgets, QtCore, QtGui
from xdg.IconTheme import getIconPath


class SimpleResult(QtWidgets.QWidget):
    def __init__(self, name, icon):
        super().__init__()
        self.layout = QtWidgets.QHBoxLayout(self)
        print(icon)
        self.icon = QtGui.QIcon(getIconPath(icon, size=48))
        self.iconlabel = QtWidgets.QLabel()
        self.iconlabel.setPixmap(self.icon.pixmap(48, 48))

        self.label = QtWidgets.QLabel(name)

        self.layout.addWidget(self.iconlabel)
        self.layout.addWidget(self.label)
        self.layout.addStretch()

        self.setStyleSheet("""
            font-size: 24px;
        """)

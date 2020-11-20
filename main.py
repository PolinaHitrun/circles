import random

import sys

from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5.QtGui import QPainter
from PyQt5.QtGui import QColor
from PyQt5 import uic


class Example(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('ui.ui', self)

        self.press = None
        self.coords = [400, 300]
        self.flag = False
        self.pushButton.clicked.connect(self.edit)

    def edit(self):
        self.flag = True
        self.repaint()

    def paintEvent(self, event):
        if self.flag:
            self.qp = QPainter()
            self.qp.begin(self)
            self.draw()
            self.qp.end()

    def draw(self):
        # self.qp.setBrush(QColor(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)))
        self.qp.setBrush(QColor(255, 204, 0))
        radius = random.randint(20, 200)
        self.qp.drawEllipse(self.coords[0] - radius, self.coords[1] - radius, 2 * radius, 2 * radius)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec())
import sys
from PyQt5.QtWidgets import QWidget, QApplication, QPushButton
from PyQt5.QtGui import QPainter, QColor, QBrush

import random


class SampleWindow(QWidget):

    def __init__(self):
        self.started = False
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(300, 300, 300, 300)
        self.setWindowTitle('Git и окружности')
        self.show()
        self.btn = QPushButton('Начать', self)
        self.btn.resize(100, 25)
        self.btn.show()
        self.btn.clicked.connect(self.start)

    def start(self):
        self.started = not (self.started)
        self.update()

    def paintEvent(self, e):
        if self.started:
            qp = QPainter()
            qp.begin(self)
            col = QColor(0, 0, 0)
            col.setNamedColor('#ffff00')
            qp.setPen(col)

            qp.setBrush(QColor(255, 255, 0))
            rx, ry = random.randint(30, 270), random.randint(30, 270)
            rw = random.randint(10, 60)

            qp.drawEllipse(rx, ry, rw, rw)
            qp.end()
            self.update()


if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)
    window = SampleWindow()
    window.show()
    sys.exit(app.exec())

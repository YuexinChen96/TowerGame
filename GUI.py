import sys
from PyQt5.QtWidgets import QWidget, QApplication
from PyQt5.QtGui import QPainter, QColor, QPen, QBrush
from PyQt5.QtCore import Qt

x_start, y_start = 340, 90
x_end, y_end = 940, 690



class GUI(QWidget):
    road = []

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(0, 0, 1000, 800)
        self.setWindowTitle('Tower Game')

    def paintEvent(self, e):
        p = QPainter()
        p.begin(self)
        p.setPen(QColor(0,0,0))
        # [340, 90] -- [940, 690]
        for i in range(21):
            p.drawLine(340, 90 + 30 * i, 940, 90 + 30 * i)
            p.drawLine(340 + 30 * i, 90, 340 + 30 * i, 690)
        print(self.road)
        if self.road == []:
            pass
        else:
            brush = QBrush(Qt.SolidPattern)
            p.setBrush(brush)
            for r in self.road:
                p.drawRect(340 + r[0] * 30, 90, 30, 30)
        p.end()
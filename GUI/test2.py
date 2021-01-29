from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5 import QtCore
from PyQt5 import QtGui
from PyQt5.QtWidgets import QWidget, QApplication
import threading
import time
import random
 
def randomcolor():
    colorArr = ['1','2','3','4','5','6','7','8','9','A','B','C','D','E','F']
    color = ""
    for i in range(6):
        color += colorArr[random.randint(0,14)]
    return "#"+color
 
 
def update_circle_color(mySig):
    while (True):
        time.sleep(2)
        mySig.signal_update_switch_state.emit(1, 0, 1, 0)
    pass
 
class MySignal(QObject):
    signal_update_switch_state = pyqtSignal(int, int, int, int)
 
class DrawCircles(QWidget):
 
    def __init__(self, parent=None):
        QWidget.__init__(self, parent)
        # setGeometry(x_pos, y_pos, width, height)
        self.setGeometry(0, 40, 258, 30)
        self.setWindowTitle('Draw circles')
        self.first_circle = 0
        self.second_circle = 0
        self.third_circle = 0
        self.fourth_circle = 0
 
 
    def updateCircleValues(self, first_circle, second_circle, third_circle, fourth_circle):
        self.first_circle = first_circle
        self.second_circle = second_circle
        self.third_circle = third_circle
        self.fourth_circle = fourth_circle
        self.update()
 
    def paintEvent(self, event):
        paint = QPainter()
        paint.begin(self)
        paint.setPen(QColor(QtCore.Qt.white))
        # paint.setBrush((QtCore.Qt.green if self.first_circle == 1 else QtCore.Qt.red))
        paint.setBrush(QColor(randomcolor()))
        paint.drawEllipse(0, 10, 15, 15);
        # paint.setBrush((QtCore.Qt.green if self.second_circle == 1 else QtCore.Qt.red))
        paint.setBrush(QColor(randomcolor()))
        paint.drawEllipse(20, 10, 15, 15);
        # paint.setBrush((QtCore.Qt.green if self.third_circle == 1 else QtCore.Qt.red))
        paint.setBrush(QColor(randomcolor()))
        paint.drawEllipse(40, 10, 15, 15);
        # paint.setBrush((QtCore.Qt.green if self.fourth_circle == 1 else QtCore.Qt.red))
        paint.setBrush(QColor(randomcolor()))
        paint.drawEllipse(60, 10, 15, 15);
        paint.end()
 
        # paint.begin(self)
        # # optional
        # paint.setRenderHint(QPainter.Antialiasing)
        # # make a white drawing background
        # paint.setBrush(Qt.white)
        # paint.drawRect(event.rect())
        # # for circle make the ellipse radii match
        # radx = 100
        # rady = 100
        # # draw red circles
        # paint.setPen(Qt.red)
        # for k in range(125, 220, 10):
        #     center = QPoint(k, k)
        #     # optionally fill each circle yellow
        #     paint.setBrush(Qt.yellow)
        #     paint.drawEllipse(center, radx, rady)
        # paint.end()
 
app = QApplication([])
 
mySig = MySignal()
circles = DrawCircles()
circles.show()
 
mySig.signal_update_switch_state.connect(circles.updateCircleValues)
 
t1 = threading.Thread(target=update_circle_color, args=(mySig,))
t1.start()
 
app.exec_()
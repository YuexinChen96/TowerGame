import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QWidget, QApplication
from PyQt5.QtGui import *
from PyQt5.QtCore import *

x_start, y_start = 340, 90
x_end, y_end = 940, 690



class GUI(QWidget):
    road = []
    tower = []

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(0, 0, 1000, 800)
        self.setWindowTitle('Tower Game')

    def paintEvent(self, e):
        p = QPainter()
        p.begin(self)
        # draw background
        self.paintStaticBoard(e, p)

        #draw road
        if self.road == []:
            pass
        else:
            brush = QBrush(Qt.SolidPattern)
            p.setBrush(brush) 
            p.setBrush(QColor(145,135,135))#grey color
            for r in self.road:
                p.drawRect(340 + r[0] * 30, 90, 30, 30) #---------need change algorithm

        

        p.end()

    def paintStaticBoard(self, e, p):
        # [340, 90] -- [940, 690] draw board
        p.setPen(QColor(0,0,0))
        for i in range(21):
            p.drawLine(340, 90 + 30 * i, 940, 90 + 30 * i)
            p.drawLine(340 + 30 * i, 90, 340 + 30 * i, 690)
        print(self.road)

        #draw tower button
        brush = QBrush(Qt.SolidPattern)
        p.setBrush(brush)
        p.setBrush(QColor(255,255,255)) #white color
        p.drawEllipse(50, 700, 40, 40)
        p.setBrush(QColor(0,0,255)) #blue color
        p.drawEllipse(110, 700, 40, 40)
        p.setBrush(QColor(255,255,0)) #yellow color
        p.drawEllipse(170, 700, 40, 40)
        p.setBrush(QColor(255,0,0)) #red color
        p.drawEllipse(230, 700, 40, 40)


    #https://blog.csdn.net/leemboy/article/details/80462632
    #https://www.cnblogs.com/liming19680104/p/10355888.html
    def mousePressEvent(self, e):
        if e.buttons() == QtCore.Qt.LeftButton:
            x = e.x()
            y = e.y()
            print(x,y)

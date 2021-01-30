import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QWidget, QApplication
from PyQt5.QtGui import *
from PyQt5.QtCore import *

from Tower import Tower
import Road

x_start, y_start = 340, 90
x_end, y_end = 940, 690



class GUI(QWidget):
    road = [[0,0],[0,1],[1,1],[2,1],[3,1],[4,1],[5,1],[6,1],[7,1],[8,1],[9,1],[9,2],[9,3],[9,4],[9,5],[9,6]]
    tower = []
    select = 0 # 0 - empty / 1 - white / 2 - blue / 3 - yellow / 4 - red
    gold = 0

    def __init__(self):
        super().__init__()
        self.initUI()
        #set up gold
        self.gold = 1000

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
            p.setBrush(QColor(145,135,135))#grey color
            for r in self.road:
                p.drawRect(340 + r[0] * 30, 90 + r[1] * 30, 30, 30) #---------need change algorithm

        #draw select
        if self.select == 0:
            pass
        else:
            if self.select == 1:
                p.setBrush(QColor(255,255,255))
            elif self.select == 2:
                p.setBrush(QColor(0,0,255))
            elif self.select == 3:
                p.setBrush(QColor(255,255,0))
            elif self.select == 4:
                p.setBrush(QColor(255,0,0))
            p.drawEllipse(60, 610, 40, 40)

        #draw block on board
        for t in self.tower:
            if t.type == 1:
                p.setBrush(QColor(255,255,255))
            elif t.type == 2:
                p.setBrush(QColor(0,0,255))
            elif t.type == 3:
                p.setBrush(QColor(255,255,0))
            elif t.type == 4:
                p.setBrush(QColor(255,0,0))
            p.drawEllipse(340 + t.x * 30, 90 + t.y * 30, 30, 30)

        p.end()

    def paintStaticBoard(self, e, p):
        # [340, 90] -- [940, 690] draw board
        p.setPen(QColor(0,0,0))
        for i in range(21):
            p.drawLine(340, 90 + 30 * i, 940, 90 + 30 * i)
            p.drawLine(340 + 30 * i, 90, 340 + 30 * i, 690)
        print(self.road)
        print(self.select)

        #draw select area
        p.drawRect(50, 600, 60, 60)

        #draw gold
        p.setFont(QFont("Arial", 30))
        p.drawRect(0, 0, 160, 70)
        p.drawText(20, 50, str(self.gold))

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
            if x > 50 and x < 90 and y > 700 and y < 740:
                self.select = 1
            elif x > 110 and x < 150 and y > 700 and y < 740:
                self.select = 2
            elif x > 170 and x < 210 and y > 700 and y < 740:
                self.select = 3
            elif x > 230 and x < 270 and y > 700 and y < 740:
                self.select = 4
            elif x < 340 or x > 940 or y < 90 or y > 690:
                self.select = 0 # select empty space return to empty select

            #select and put tower into board
            if self.select != 0 and x >= 340 and x <= 940 and y >= 90 and y <= 690:
                re_x = int((x - 340) / 30)
                re_y = int((y - 90) / 30) 
                #  ========================================yao kao lv he lu de pan ding
                t = Tower(re_x, re_y, self.select)
                self.tower.append(t)



            self.update()
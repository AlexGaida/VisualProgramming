from PyQt5 import QtGui
from PyQt5.QtWidgets import QApplication, QMainWindow
import sys

from PyQt5.QtGui import QPainter, QBrush, QPen
from PyQt5.QtCore import Qt

class Window(QMainWindow):
    def __init__(self):
        super().__init__()
        self.title = "PyQt5 Drawing Canvas"
        self.top = 150
        self.left = 150
        self.width = 1000
        self.height = 1000
        self.InitWindow()

    def InitWindow(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.top, self.left, self.width, self.height)
        self.show()
        
    def paintEvent(self, event):
        painter = QPainter(self)
        painter2 = QPainter(self)
        init_top = 20
        init_left = 5
        for t in range(0, 35):
            for i in range(0, 20):
                x = init_left + 60 * t
                y = init_top + 60 * i
                painter2.setBrush(QBrush(Qt.darkRed, Qt.SolidPattern))
                painter2.drawEllipse(x, y, 8, 8)
                painter.setBrush(QBrush(Qt.yellow, Qt.CrossPattern))
                painter.setPen(QPen(Qt.red, 5, Qt.DashDotDotLine))
                painter.drawEllipse(x, y, 50, 50)
            
        
if __name__ == "__main__":
    app = QApplication([])
    app.setStyle('Fusion')
    win = Window()
    win.show()
    app.exec()

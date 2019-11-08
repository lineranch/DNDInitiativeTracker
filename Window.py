from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QPushButton


class WindowExample(QWidget):
    initHeight = 500
    initWidth = 500
    extraCount = 0

    def __init__(self):
        super().__init__()
        self.createWindow()


    def createWindow(self):
        self.layout = QVBoxLayout()
        startButt = QPushButton("Add Monster")
        #self.setFont(QFont('SansSerif', 100))

        self.layout.addWidget(startButt)
        startButt.clicked.connect(self.addMonster)

        self.setLayout(self.layout)
        self.resize(self.initHeight, self.initWidth)

    def addMonster(self):
        self.extraCount += 1
        monster = QPushButton("Monster " + str(self.extraCount))
        self.layout.addWidget(monster)
        self.setLayout(self.layout)
        monster.clicked.connect(monster.deleteLater())




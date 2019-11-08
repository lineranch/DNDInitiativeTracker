from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QPushButton, QInputDialog


class Generator(QWidget):
    initHeight = 500
    initWidth = 500
    extraCount = 0

    def __init__(self):
        super().__init__()
        self.generateCreatures(self.getCreatureNum())
        self.resize(self.initHeight, self.initWidth)



    def getCreatureNum(self):
        numOfCreatures = QInputDialog.getInt(self, "Number of Creatures", "Value", 0, 0, 100, 1)
        return numOfCreatures

    def generateCreatures(self, numberOf):
        numOfCreatures = QInputDialog.getInt(self, "Number of Creatures", "Value", 0, numberOf[0], 100, 1)
        pass



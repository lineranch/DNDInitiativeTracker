from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QPushButton, QInputDialog, QTableWidget, QTableWidgetItem, \
    QStackedWidget, QFrame, QSplitter, QHBoxLayout


class Generator(QWidget):
    initHeight = 500
    initWidth = 500
    extraCount = 0

    def __init__(self):
        super().__init__()


        self.resize(self.initHeight, self.initWidth)

        boxLayout = QHBoxLayout()

        creatureDetails = QFrame()
        creatureDetails.setFrameShape(QFrame.StyledPanel)

        creatureTable = QTableWidget(self.getCreatureNum()[0],5)
        creatureTable.setFrameShape(QFrame.StyledPanel)
        creatureTable.setHorizontalHeaderItem(0,QTableWidgetItem("Creature Name"))
        creatureTable.setHorizontalHeaderItem(0, QTableWidgetItem("Creature Initiative"))

        creatureOrder = QFrame()

        topSplitter = QSplitter(Qt.Horizontal)
        topSplitter.addWidget(creatureDetails)
        topSplitter.addWidget(creatureTable)

        mainSplitter = QSplitter(Qt.Vertical)
        mainSplitter.addWidget(topSplitter)
        mainSplitter.addWidget(creatureOrder)

        boxLayout.addWidget(mainSplitter)
        self.setLayout(boxLayout)

    def getCreatureNum(self):
        numberOfCreatures = QInputDialog.getInt(self, "Get Number of Creatures", "Input a number", 0, 0, 100, 1)
        return  numberOfCreatures




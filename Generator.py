from DNDInitiativeTracker import Monster
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QPushButton, QInputDialog, QTableWidget, QTableWidgetItem, \
    QStackedWidget, QFrame, QSplitter, QHBoxLayout, QLabel


class Generator(QWidget):
    initHeight = 1000
    initWidth = 1000
    extraCount = 0
    MonsterOrder = []

    def __init__(self):
        super().__init__()

        boxLayout = QHBoxLayout()

        creatureTable = QFrame()
        #creatureInfo = QFrame()
        creatureOrder = QFrame()

        creatureTable.setFrameShape(QFrame.StyledPanel)
        #creatureInfo.setFrameShape(QFrame.StyledPanel)
        creatureOrder.setFrameShape(QFrame.StyledPanel)

        topRightPanelButtons = QSplitter(Qt.Horizontal)
        addMonster = QPushButton("Add Monster")
        addMonster.clicked.connect(self.addMonster)
        removeMonster = QPushButton("Remove Monster")
        removeMonster.clicked.connect(self.removeMonster)
        topRightPanelButtons.addWidget(addMonster)
        topRightPanelButtons.addWidget(removeMonster)


        topRightPanel = QSplitter(Qt.Vertical)
        topRightPanel.addWidget(topRightPanelButtons)
        topRightPanel.addWidget(creatureTable)

        list = [100, 500]
        topRightPanel.setSizes(list)

        topPanel = QSplitter(Qt.Horizontal)
        #topPanel.addWidget(creatureInfo)
        topPanel.addWidget(topRightPanel)

        list = [100, 500]
        topPanel.setSizes(list)

        self.mainPanel = QSplitter(Qt.Vertical)
        self.mainPanel.addWidget(topPanel)
        self.mainPanel.addWidget(creatureOrder)

        list = [300,300]
        self.mainPanel.setSizes(list)

        self.resize(self.initHeight, self.initWidth)
        boxLayout.addWidget(self.mainPanel)
        self.setLayout(boxLayout)

    def addMonster(self):
        monster = Monster.Monster()
        print(monster)
        self.mainPanel.addWidget(QLabel(monster.__str__()))



    def removeMonster(self):
        print("Remove")



from DNDInitiativeTracker import Monster
from DNDInitiativeTracker import customItem
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QPushButton, QFrame, QSplitter, QHBoxLayout, QLabel, QListWidget, \
    QLineEdit


class Generator(QWidget):
    initHeight = 1000
    initWidth = 1000
    extraCount = 0

    def __init__(self):
        super().__init__()
        self.currentlySelected = None
        self.makeWindow()

    def addMonster(self):
        monster = Monster.Monster()
        item = customItem.CustomListWidgetItem()
        item.setText(monster.name)
        data = [monster.name, monster.health, monster.initiative]
        item.setData(Qt.UserRole,data)
        self.creatureOrder.addItem(item)



    def removeMonster(self):
        list = self.creatureOrder.selectedItems()
        if not list: return
        for item in list:
            self.creatureOrder.takeItem(self.creatureOrder.row(item))


    def displayMonster(self, item):
        data = item.data(Qt.UserRole)


        self.currentlySelected = item
        self.creatureInfo.update(data[0],data[1],data[2])

    def makeWindow(self):
        boxLayout = QHBoxLayout()

        self.creatureInfo = displayInformation()
        self.creatureOrder = QListWidget()
        self.creatureOrder.setSortingEnabled(True)
        self.creatureOrder.setFlow(self.creatureOrder.LeftToRight)
        self.creatureOrder.itemClicked.connect(self.displayMonster)
        self.creatureOrder.itemClicked.connect(self.displayMonster)

        #self.creatureInfo.setFrameShape(QFrame.StyledPanel)
        self.creatureOrder.setFrameShape(QFrame.StyledPanel)

        topRightPanelButtons = QSplitter(Qt.Horizontal)
        addMonster = QPushButton("Add Monster")
        addMonster.clicked.connect(self.addMonster)
        removeMonster = QPushButton("Remove Monster")
        removeMonster.clicked.connect(self.removeMonster)
        topRightPanelButtons.addWidget(addMonster)
        topRightPanelButtons.addWidget(removeMonster)

        topRightPanel = QSplitter(Qt.Vertical)
        topRightPanel.addWidget(topRightPanelButtons)
        topRightPanel.addWidget(self.creatureInfo)

        list = [100, 500]
        topRightPanel.setSizes(list)

        topPanel = QSplitter(Qt.Horizontal)
        topPanel.addWidget(topRightPanel)

        list = [100, 500]
        topPanel.setSizes(list)

        self.mainPanel = QSplitter(Qt.Vertical)
        self.mainPanel.addWidget(topPanel)
        self.mainPanel.addWidget(self.creatureOrder)

        list = [300, 300]
        self.mainPanel.setSizes(list)

        self.resize(self.initHeight, self.initWidth)
        boxLayout.addWidget(self.mainPanel)
        self.setLayout(boxLayout)

class displayInformation(QWidget):

    def __init__(self):
        super().__init__()
        self.monsterName = "Monster Name"
        self.monsterHealth = "Monster Health"
        self.monsterInitiatve = "Monster Initiative"

        self.labelList = [QLabel(self.monsterName),QLabel(self.monsterHealth), QLabel(self.monsterInitiatve)]
        self.editList = [QLineEdit(),QLineEdit(),QLineEdit()]

        self.layout = QVBoxLayout()
        for i in range(len(self.labelList)):
            self.layout.addWidget(self.labelList[i])
            self.layout.addWidget(self.editList[i])



        self.setLayout(self.layout)

    def update(self, name, health, init):
        self.labelList[0].setText("Name: " +  str(name))
        self.labelList[1].setText("Health: " + str(health))
        self.labelList[2].setText("Initiative: " + str(init))



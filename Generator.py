from DNDInitiativeTracker import Monster
from DNDInitiativeTracker import customItem
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QPushButton, QFrame, QSplitter, QHBoxLayout, QLabel, QListWidget, \
    QLineEdit

# Makes the application
class Generator(QWidget):
    initHeight = 1000
    initWidth = 1000

    def __init__(self):
        super().__init__()
        self.currentlySelected = None
        self.makeWindow()

    def addMonster(self):
        monster = Monster.Monster()
        item = customItem.CustomListWidgetItem()
        item.setText(monster.name)
        item.setData(Qt.UserRole,monster)
        self.creatureOrder.addItem(item)



    def removeMonster(self):
        list = self.creatureOrder.selectedItems()
        if not list: return
        for item in list:
            self.creatureOrder.takeItem(self.creatureOrder.row(item))


    def displayMonster(self, item):
        data = item.data(Qt.UserRole)
        self.currentlySelected = item
        self.creatureInfo.update(data)





    # This method is the code for the main window
    def makeWindow(self):
        boxLayout = QHBoxLayout()

        self.creatureInfo = self.displayInformation(self)
        self.creatureOrder = QListWidget()
        self.creatureOrder.setSortingEnabled(True)
        self.creatureOrder.setFlow(self.creatureOrder.LeftToRight)
        self.creatureOrder.itemClicked.connect(self.displayMonster)
        self.creatureOrder.itemClicked.connect(self.displayMonster)
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

    # This class creates an object of the widget that displays the information
    class displayInformation(QWidget):

        def __init__(self, parent):
            super().__init__()
            self.parent = parent
            self.mostRecent = None
            self.monsterName = "Monster Name"
            self.monsterHealth = "Monster Health"
            self.monsterInitiatve = "Monster Initiative"
            self.monsterAC = "Monster Armor Class"

            self.labelList = [QLabel(self.monsterName), QLabel(self.monsterHealth), QLabel(self.monsterInitiatve), QLabel(self.monsterAC)]

            self.changeNameLine = QLineEdit()
            self.changeNameLine.returnPressed.connect(self.changeName)
            self.changeHealthLine = QLineEdit()
            self.changeHealthLine.returnPressed.connect(self.changeHealth)
            changeInit = QLineEdit()
            changeMonsterAC = QLineEdit()

            self.editList = [self.changeNameLine, self.changeHealthLine, changeInit, changeMonsterAC]

            self.layout = QVBoxLayout()
            for i in range(len(self.labelList)):
                self.layout.addWidget(self.labelList[i])
                self.layout.addWidget(self.editList[i])

            self.setLayout(self.layout)

        def update(self, data):
            self.mostRecent = data
            self.labelList[0].setText("Name: " + str(data.name))
            self.labelList[1].setText("Health: " + str(data.health))
            self.labelList[2].setText("Initiative: " + str(data.initiative))
            self.labelList[3].setText("Armor Class: " + str(data.ac))


        def changeHealth(self):
            newHealth = self.changeHealthLine.text()
            if (newHealth == ""):
                return
            self.mostRecent.health = newHealth
            self.labelList[1].setText("Health: " + str(newHealth))
            self.changeHealthLine.setText("")

        def changeName(self):
            oldName = self.mostRecent.name
            newName = self.changeNameLine.text()
            if (newName == ""):
                return
            self.mostRecent.name = newName
            self.labelList[0].setText("Name: " + str(newName))
            self.changeNameLine.setText("")










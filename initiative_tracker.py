#This code is a refactored version of DNDInititativeDriver.py, Generator.py, Monster.py, and customItem.py
import sys
from functools import partial
from PyQt5.Qt import Qt
from PyQt5.QtWidgets import QApplication, QDialog, QDialogButtonBox, QHBoxLayout, QLabel, QLineEdit, QListWidget, QListWidgetItem, QPushButton, QSplitter, QWidget, QVBoxLayout



class InititativeTracker(QWidget):

    def __init__(self):
        super().__init__()
        self.makeApplication()



    def makeApplication(self):
        applicationLayout = QVBoxLayout()
        buttonLayer = self.makeButtonLayer()
        self.statLayer = MonsterInformation()
        self.orderLayer = QListWidget()
        self.orderLayer.setSortingEnabled(True)
        self.orderLayer.setFlow(self.orderLayer.LeftToRight)
        self.orderLayer.itemClicked.connect(self.displayMonster)

        applicationLayout.addLayout(buttonLayer)
        applicationLayout.addWidget(self.statLayer)
        applicationLayout.addWidget(self.orderLayer)


        self.setLayout(applicationLayout)

    def makeButtonLayer(self):
        lay = QHBoxLayout()

        addMonsterButt = QPushButton("Add Monster")
        addMonsterButt.clicked.connect(self.addMonster)
        removeMonsterButt = QPushButton("Remove Monster")
        removeMonsterButt.clicked.connect(self.removeMonster)

        lay.addWidget(addMonsterButt)
        lay.addWidget(removeMonsterButt)

        return lay

    def addMonster(self):
        monster = Monster()
        item = CustomItem(monster.name)
        item.setData(Qt.UserRole,monster)
        self.orderLayer.addItem(item)



    def removeMonster(self):
        list = self.orderLayer.selectedItems()
        if not list: return
        for item in list:
            self.orderLayer.takeItem(self.orderLayer.row(item))


    def displayMonster(self, item):
        data = item.data(Qt.UserRole)
        self.statLayer.update(data)

class MonsterInformation(QWidget):

    def __init__(self):
        super().__init__()
        self.currentlySelected = None

        self.monsterName = QLabel("Monster Name")
        self.monsterHealth = QLabel("Monster Health")
        self.monsterInitiatve = QLabel("Monster Initiative")


        self.layout = QVBoxLayout()
        self.layout.addWidget(self.monsterName)
        self.layout.addWidget(self.monsterHealth)
        self.layout.addLayout(self.makeAddSubButts())
        self.layout.addWidget(self.monsterInitiatve)

        self.setLayout(self.layout)

    def makeAddSubButts(self):
        lay = QHBoxLayout()

        self.editLine = QLineEdit()
        self.addHealth = QPushButton("Add Health")
        self.addHealth.clicked.connect(partial(self.changeHealth, self.addHealth))
        self.removeHealth = QPushButton("Remove Health")
        self.removeHealth.clicked.connect(partial(self.changeHealth, self.removeHealth))

        lay.addWidget(self.editLine)
        lay.addWidget(self.addHealth)
        lay.addWidget(self.removeHealth)

        return lay

    def changeHealth(self, btn):
        try:
            if (btn == self.addHealth):
                value = self.editLine.text()
                self.currentlySelected.health += int(value)
                self.update(self.currentlySelected)
            elif (btn == self.removeHealth):
                value = self.editLine.text()
                self.currentlySelected.health -= int(value)
                self.update(self.currentlySelected)
            self.editLine.setText("")
        except Exception:
            print("BAD INPUT")

    def update(self, item):
        self.currentlySelected = item
        self.monsterName.setText("Name: " +  str(item.name))
        self.monsterHealth.setText("Health: " + str(item.health))
        self.monsterInitiatve.setText("Initiative: " + str(item.initiative))


class CustomItem(QListWidgetItem):
    def __lt__(self, other):
        try:
            data = self.data(Qt.UserRole)
            otherData = other.data(Qt.UserRole)
            init = data.initiative
            otherInit = otherData.initiative
            return int(init) > int(otherInit)

        except Exception:
            print("Didnt work")
            return QListWidgetItem.__lt__(self, other)


class Monster():

    def __init__(self):
        data, ok = MonsterDialog.getDateTime()

        self.name = data[0]
        self.health = int(data[1])
        self.initiative = data[2]


    def __str__(self):

        return "Monster Name : " + self.name + " Monster Health: " + self.health + " Monster Init: " + self.initiative




# This block creates a window to input monster information
class MonsterDialog(QDialog):
    def __init__(self, parent = None):
        super(MonsterDialog, self).__init__(parent)

        self.nameLine = QLineEdit()
        self.healthLine = QLineEdit()
        self.initLine = QLineEdit()

        innerVBox = QVBoxLayout()
        innerHBox = QHBoxLayout()
        outerBox = QVBoxLayout()

        innerVBox.addWidget(QLabel("Enter Name:"))
        innerVBox.addWidget(self.nameLine)
        innerVBox.addWidget(QLabel("Enter Health"))
        innerVBox.addWidget(self.healthLine)
        innerVBox.addWidget(QLabel("Enter Initiative"))
        innerVBox.addWidget(self.initLine)

        #Using the dialog class, I made a button for okay and cancel
        buttons = QDialogButtonBox(
            QDialogButtonBox.Ok | QDialogButtonBox.Cancel,
            Qt.Horizontal, self)
        buttons.accepted.connect(self.accept)
        buttons.rejected.connect(self.reject)

        innerHBox.addWidget(buttons)

        outerBox.addLayout(innerVBox)
        outerBox.addLayout(innerHBox)

        self.setLayout(outerBox)

    # get current date and time from the dialog
    def dateTime(self):
        data = []
        data.append(self.nameLine.text())
        data.append(self.healthLine.text())
        data.append(self.initLine.text())
        return data

    # static method to create the dialog and return (date, time, accepted)
    @staticmethod
    def getDateTime(parent = None):
        dialog = MonsterDialog(parent)
        result = dialog.exec_()
        data = dialog.dateTime()

        return (data, result == QDialog.Accepted)

# https://stackoverflow.com/questions/18196799/how-can-i-show-a-pyqt-modal-dialog-and-get-data-out-of-its-controls-once-its-clo



def main():
    app = QApplication(sys.argv)
    ex = InititativeTracker()
    ex.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()
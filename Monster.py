import sys
from PyQt5.QtWidgets import QLineEdit, QVBoxLayout, QHBoxLayout, QLabel, QDialog, \
    QDialogButtonBox
from PyQt5.QtCore import Qt

class Monster():

    def __init__(self):
        # A multi inpit dialog window poops up when a monster object is created
        data, ok = MonsterDialog.getmonsterData()

        self.name = data[0]
        self.health = data[1]
        self.initiative = data[2]
        self.ac = data[3]

    def __str__(self):

        return "Monster Name : " + self.name + " Monster Health: " + self.health + " Monster Init: " + self.initiative




# This block creates a window to input monster information
class MonsterDialog(QDialog):
    def __init__(self, parent = None):
        super(MonsterDialog, self).__init__(parent)

        self.nameLine = QLineEdit()
        self.healthLine = QLineEdit()
        self.initLine = QLineEdit()
        self.acLine = QLineEdit()

        innerVBox = QVBoxLayout()
        innerHBox = QHBoxLayout()
        outerBox = QVBoxLayout()

        innerVBox.addWidget(QLabel("Enter Name:"))
        innerVBox.addWidget(self.nameLine)
        innerVBox.addWidget(QLabel("Enter Health"))
        innerVBox.addWidget(self.healthLine)
        innerVBox.addWidget(QLabel("Enter Initiative"))
        innerVBox.addWidget(self.initLine)
        innerVBox.addWidget(QLabel("Enter Armor Class"))
        innerVBox.addWidget(self.acLine)

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
    def monsterData(self):
        data = []
        data.append(self.nameLine.text())
        data.append(self.healthLine.text())
        data.append(self.initLine.text())
        data.append(self.acLine.text())
        return data

    # static method to create the dialog and return (date, time, accepted)
    @staticmethod
    def getmonsterData(parent = None):
        dialog = MonsterDialog(parent)
        result = dialog.exec_()
        data = dialog.monsterData()

        return (data, result == QDialog.Accepted)

# https://stackoverflow.com/questions/18196799/how-can-i-show-a-pyqt-modal-dialog-and-get-data-out-of-its-controls-once-its-clo
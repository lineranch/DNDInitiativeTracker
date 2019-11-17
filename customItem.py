from PyQt5.QtWidgets import QListWidgetItem
from PyQt5.QtCore import Qt

class CustomListWidgetItem(QListWidgetItem):
    #This is a comparator for the QList. This compares a monsters initiative
    def __lt__(self, other):
        print("Here")
        try:
            data = self.data(Qt.UserRole)
            otherData = other.data(Qt.UserRole)
            init = data.initiative
            otherInit = otherData.initiative
            print(self.data(Qt.UserRole))
            return int(init) > int(otherInit)

        except Exception:
            print("Didnt work")
            return QListWidgetItem.__lt__(self, other)

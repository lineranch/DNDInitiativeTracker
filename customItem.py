from PyQt5.QtWidgets import QApplication, QListWidget, QListWidgetItem
from PyQt5.QtCore import Qt

class CustomListWidgetItem(QListWidgetItem):
    def __lt__(self, other):
        print("Here")
        try:
            data = self.data(Qt.UserRole)
            otherData = other.data(Qt.UserRole)
            init = data[2]
            otherInit = otherData[2]
            print(self.data(Qt.UserRole))
            return int(init) > int(otherInit)

        except Exception:
            print("Didnt work")
            return QListWidgetItem.__lt__(self, other)

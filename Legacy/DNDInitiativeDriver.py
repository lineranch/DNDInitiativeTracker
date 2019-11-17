import sys
from PyQt5.QtWidgets import QApplication
from DNDInitiativeTracker import Generator

if __name__ == "__main__":
    print(sys.path)
    sys.path.append("Generator.py")
    app = QApplication(sys.argv)
    ex = Generator.Generator()                #Instead of making an instance of a window (window = QWidget), We can make this object
    ex.show()
    sys.exit(app.exec())
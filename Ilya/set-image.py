from PyQt5.QtWidgets import *
from PyQt5.QtGui import QPixmap
import sys


class Window(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Image")
        self.setGeometry(0, 0, 400, 300)
        self.label = QLabel(self)
        self.pixmap = QPixmap('wood.jpg')
        self.label.setPixmap(self.pixmap)
        self.label.resize(200, 200)
        btn = QPushButton('Hi', self)
        self.show()


# create pyqt5 app
App = QApplication(sys.argv)

# create the instance of our Window
window = Window()

# start the app
sys.exit(App.exec())
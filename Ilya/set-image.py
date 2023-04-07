# importing the required libraries

from PyQt5.QtWidgets import *
from PyQt5.QtGui import QPixmap
import sys

print(sys.argv)
app = QApplication(sys.argv)
window = QWidget()
window.setFixedSize(500, 500)
input_main = QLineEdit(window)
input_main.resize(300, 100)
input = QLineEdit(window)
button = QPushButton(window)
button.setGeometry(200, 200, 400, 400)
button.setStyleSheet('''
    background-image: url(rsz_equal-sign.jp*g);
''')

window.show()
app.exec()

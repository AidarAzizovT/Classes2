from PyQt5.QtWidgets import QApplication,\
    QLabel, QWidget, QPushButton, QComboBox, QLineEdit, QShortcut
from PyQt5.QtGui import QFont, QKeySequence, QPixmap
from PyQt5.Qt import QTimer
from PyQt5.QtCore import pyqtSlot
def do_something():
    if button.underMouse():
        print('Yes')

def test():
    print('It is working')

app = QApplication([])
window = QWidget()
window.resize(200, 200)
button = QPushButton('Hello', window)

px_logo = QPixmap('ball.png.png')
label = QLabel(window)
#label.setPixmap(px_logo)
print()
#button.setStyleSheet('background : green; color : white;')
button.setToolTip('Aidar')
shorcut = QShortcut(QKeySequence('+'), window)
shorcut.activated.connect(test)
timer = QTimer()
timer.timeout.connect(do_something)
timer.setInterval(5000)
timer.start(100)




window.show()
app.exec()


#
#'14 + 5'
#430-6
#arr = ['14', '+', '5']
#'4+5+3'




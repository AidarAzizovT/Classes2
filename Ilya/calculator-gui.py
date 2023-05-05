from PyQt5.QtWidgets import QApplication,\
    QLabel, QWidget, QPushButton, QComboBox, QLineEdit
from PyQt5.QtGui import QFont
from Ilya.calculating import calculate


def execute():
    try:
        calculation = calculate(input.text())
        input.setText(str(calculation))
    except:
        input.setText('Error')


app = QApplication([])
window = QWidget()
window.resize(500, 400)

input = QLineEdit(window)
input.setGeometry(30, 30, 440, 70)
input.setFont(QFont('Arial', 18))
input.setFrame(False)
input.returnPressed.connect(execute
                            )

button = QPushButton(parent=window, text='=')
button.setFont(QFont('Arial', 18))
button.setGeometry(380, 310, 90, 60)
button.clicked.connect(execute)


window.show()
app.exec()
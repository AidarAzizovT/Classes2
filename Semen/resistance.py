from PyQt5.QtWidgets import QApplication,\
    QLabel, QWidget, QPushButton, QComboBox, QLineEdit
from PyQt5.QtGui import QFont

MATERIALS = {'медь': 100, 'аллюминий':200, 'золото':10}

app = QApplication([])
window = QWidget()
window.resize(600, 600)


label = QLabel()
label.setParent(window)
label.setText('Программа для подсчета сопротивления проводника')
label.move(10, 100)
label.setFont(QFont('Arial', 14))

combobox = QComboBox()
combobox.addItems([])
combobox.setParent(window)
combobox.setGeometry(200, 200, 200, 50)

#65897 + 7 + 698
length_input = QLineEdit()
length_input.setParent(window)
length_input.setGeometry(100, 300, 150, 50)


square_input = QLineEdit()
square_input.setParent(window)
square_input.setGeometry(300, 300, 150, 50)

button = QPushButton()
button.setParent(window)
button.setText('Посчитать сопротивление')
button.setGeometry(200, 400, 200, 50)

result_label = QLabel()
result_label.setParent(window)
result_label.move(150, 500)
result_label.setFont(QFont('Arial', 14))
result_label.setText('Результат: ')


value_label = QLineEdit()
value_label.setParent(window)
value_label.setGeometry(300, 500, 150, 50)

def calculate():
    length_value = length_input.text()
    square_value = square_input.text()
    choose_material = combobox.currentText()
    calculated_resistanse = MATERIALS[choose_material] * int(square_value) / int(length_value)

    value_label.setText(str(calculated_resistanse))
    print('Результат: ' + str(calculated_resistanse))


button.clicked.connect(calculate)
window.show()
app.exec()
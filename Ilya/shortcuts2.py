from PyQt5.QtWidgets import QApplication, QMainWindow, QAction, QShortcut
from PyQt5.QtGui import QKeySequence
from PyQt5.QtCore import Qt

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # Create a menu item
        self.menu = self.menuBar().addMenu("File")
        self.action = QAction("Open", self)
        self.action.setShortcut(QKeySequence(Qt.CTRL + Qt.Key_O))
        self.action.triggered.connect(self.open_file)
        self.menu.addAction(self.action)

        # Create a shortcut for the same action
        self.shortcut = QShortcut(QKeySequence(Qt.CTRL + Qt.Key_O), self)
        self.shortcut.activated.connect(self.open_file)

    def open_file(self):
        # Do something when the menu item or shortcut is triggered
        print('Hi')
        pass

if __name__ == "__main__":
    app = QApplication([])
    window = MainWindow()
    window.show()
    app.exec_()
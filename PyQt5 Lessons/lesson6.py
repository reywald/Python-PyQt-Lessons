import sys
from PyQt5 import QtWidgets


class Window(QtWidgets.QWidget):

    def __init__(self):
        super().__init__()

        self.init_ui()

    def init_ui(self):
        self.ledit = QtWidgets.QLineEdit()
        self.btn1 = QtWidgets.QPushButton("Clear")
        self.btn2 = QtWidgets.QPushButton("Print")

        vbox = QtWidgets.QVBoxLayout()
        vbox.addWidget(self.ledit)
        vbox.addWidget(self.btn1)
        vbox.addWidget(self.btn2)

        self.setLayout(vbox)
        self.setWindowTitle("PyQt5 Lesson 5")

        self.btn1.clicked.connect(self.btn_click)
        self.btn2.clicked.connect(self.btn_click)

        self.show()

    def btn_click(self):
        sender = self.sender()
        if sender.text() == "Print":
            print(self.ledit.text())
        else:
            self.ledit.clear()


app = QtWidgets.QApplication(sys.argv)
window = Window()
sys.exit(app.exec_())

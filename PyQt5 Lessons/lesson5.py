import sys
from PyQt5 import QtWidgets


class Window(QtWidgets.QWidget):

    def __init__(self):
        super().__init__()

        self.init_ui()

    def init_ui(self):
        self.btn = QtWidgets.QPushButton('Push Me')
        self.lbl = QtWidgets.QLabel('I have not been clicked yet')

        hbox = QtWidgets.QHBoxLayout()
        hbox.addStretch()
        hbox.addWidget(self.lbl)
        hbox.addStretch()

        vbox = QtWidgets.QVBoxLayout()
        vbox.addWidget(self.btn)
        vbox.addLayout(hbox)

        self.setLayout(vbox)
        self.setWindowTitle("PyQt5 Lesson 5")

        self.btn.clicked.connect(self.btn_click)

        self.show()

    def btn_click(self):
        self.lbl.setText('I have been clicked')


app = QtWidgets.QApplication(sys.argv)
window = Window()
sys.exit(app.exec_())

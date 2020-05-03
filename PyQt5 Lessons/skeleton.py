import sys
from PyQt5.QtWidgets import (
    QLineEdit, QSlider, QPushButton, QVBoxLayout, QApplication, QWidget)
from PyQt5.QtCore import Qt


class Window(QWidget):

    def __init__(self):
        super().__init__()

        self.init_ui()

    def init_ui(self):
        self.btn = QPushButton('Push Me')
        self.lbl = QLabel('I have not been clicked yet')

        vbox = QVBoxLayout()
        vbox.addWidget(self.lbl)
        vbox.addWidget(self.btn)

        self.setLayout(vbox)
        self.setWindowTitle("PyQt5 Lesson 5")

        self.show()


app = QApplication(sys.argv)
window = Window()
sys.exit(app.exec_())

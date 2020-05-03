import sys
from PyQt5.QtWidgets import (
    QLabel, QCheckBox, QPushButton, QVBoxLayout, QApplication, QWidget)


class Window(QWidget):

    def __init__(self):
        super().__init__()

        self.init_ui()

    def init_ui(self):
        self.lbl = QLabel()
        self.check = QCheckBox("Do you like dogs?")
        self.btn = QPushButton('Push Me')

        vbox = QVBoxLayout()
        vbox.addWidget(self.lbl)
        vbox.addWidget(self.check)
        vbox.addWidget(self.btn)

        self.setLayout(vbox)
        self.setWindowTitle("PyQt5 Lesson 5")

        self.btn.clicked.connect(lambda: self.btn_click(
            self.check.isChecked(), self.lbl))

        self.show()

    def btn_click(self, checked: bool, label: QLabel):
        if checked:
            label.setText("I guesss you like dogs")
        else:
            label.setText("Dog hater then")


app = QApplication(sys.argv)
window = Window()
sys.exit(app.exec_())

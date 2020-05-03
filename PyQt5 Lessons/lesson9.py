import sys
from PyQt5.QtWidgets import (
    QLabel, QRadioButton, QPushButton, QVBoxLayout, QApplication, QWidget)


class Window(QWidget):

    def __init__(self):
        super().__init__()

        self.init_ui()

    def init_ui(self):
        self.label = QLabel('Which do you like best?')
        self.dog = QRadioButton("Dogs")
        self.cat = QRadioButton("Cats")
        self.button = QPushButton("Select")

        vbox = QVBoxLayout()
        vbox.addWidget(self.label)
        vbox.addWidget(self.dog)
        vbox.addWidget(self.cat)
        vbox.addWidget(self.button)

        self.setLayout(vbox)
        self.setWindowTitle("PyQt5 Lesson 9")

        # Connect the button's signal to a slot
        self.button.clicked.connect(
            lambda: self.btn_click(self.dog.isChecked(), self.label))

        self.show()

    def btn_click(self, checked: bool, label: QLabel):
        if checked:
            label.setText("I guess you like dogs")
        else:
            label.setText("So it's cats for you")


app = QApplication(sys.argv)
window = Window()
sys.exit(app.exec_())

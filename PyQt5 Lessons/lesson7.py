import sys
from PyQt5.QtWidgets import (
    QLineEdit, QSlider, QPushButton, QVBoxLayout, QApplication, QWidget)
from PyQt5.QtCore import Qt


class Window(QWidget):

    def __init__(self):
        super().__init__()

        self.init_ui()

    def init_ui(self):
        self.ledit = QLineEdit()
        self.btn1 = QPushButton("Clear")
        self.btn2 = QPushButton("Print")

        # Create and configure the slider
        self.slider = QSlider(Qt.Horizontal)
        self.slider.setMaximum(99)
        self.slider.setValue(25)
        self.slider.setTickInterval(10)
        self.slider.setTickPosition(QSlider.TicksBelow)

        # Create the box layout to place the GUI components
        vbox = QVBoxLayout()
        vbox.addWidget(self.ledit)
        vbox.addWidget(self.btn1)
        vbox.addWidget(self.btn2)
        vbox.addWidget(self.slider)

        self.setLayout(vbox)
        self.setWindowTitle("PyQt5 Lesson 5")

        # Connect the components' signals to their respective slots
        self.btn1.clicked.connect(
            lambda: self.btn_click(self.btn1, "Hello from Clear"))
        self.btn2.clicked.connect(
            lambda: self.btn_click(self.btn2, "Hello from Print"))
        self.slider.valueChanged.connect(self.v_change)

        self.show()

    def btn_click(self, button: QPushButton, string: str):
        """ This slot is used to handle the clicked signal from the QPushButtons """
        if button.text() == "Print":
            print(self.ledit.text())
        else:
            self.ledit.clear()
        print(string)

    def v_change(self):
        """ This slot is used to handle the valueChanged signal from the QSlider """
        my_value = str(self.slider.value())
        self.ledit.setText(my_value)


app = QApplication(sys.argv)
window = Window()
sys.exit(app.exec_())

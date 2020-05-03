import sys
from PyQt5 import QtWidgets, QtGui


""" 
    Create a simple QtWidgets window, add two labels. One label will 
    hold text, and the other will hold an image.
"""


def window():
    app = QtWidgets.QApplication(sys.argv)
    w = QtWidgets.QWidget()

    label1 = QtWidgets.QLabel(w)
    label1.setText("Hello World")

    label2 = QtWidgets.QLabel(w)
    label2.setPixmap(QtGui.QPixmap("Resources/internet-icon.png"))

    label1.move(100, 20)
    label2.move(120, 90)

    w.setWindowTitle("PyQt5 Lesson 2")
    w.setGeometry(100, 100, 300, 200)
    w.show()
    sys.exit(app.exec_())


window()

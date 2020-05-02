import sys
from PyQt5 import QtWidgets


""" Create a simple QtWidgets window """


def window():
    app = QtWidgets.QApplication(sys.argv)
    w = QtWidgets.QWidget()
    w.setWindowTitle("PyQt5 Lesson 1")
    w.show()
    sys.exit(app.exec_())


window()

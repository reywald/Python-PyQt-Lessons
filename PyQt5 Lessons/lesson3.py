import sys
from PyQt5 import QtWidgets, QtGui


""" Create a simple QtWidgets window. Add a button and label """


def window():
    app = QtWidgets.QApplication(sys.argv)
    w = QtWidgets.QWidget()
    w.setWindowTitle("PyQt5 Lesson 1")

    btn = QtWidgets.QPushButton(parent=w)
    btn.setText("Push Me")
    btn.setIcon(QtGui.QIcon("internet-icon.png"))
    lbl = QtWidgets.QLabel(parent=w)
    lbl.setText("Look at Me")
    btn.move(100, 50)
    lbl.move(110, 100)

    w.show()
    sys.exit(app.exec_())


window()

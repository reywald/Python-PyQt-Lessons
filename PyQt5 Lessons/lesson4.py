import sys
from PyQt5 import QtWidgets, QtGui


""" 
    Create a simple QtWidgets window. Use a horizontal and vertical layout 
    to add a label and button
"""


def window():
    app = QtWidgets.QApplication(sys.argv)
    w = QtWidgets.QWidget()
    w.setWindowTitle("PyQt5 Lesson 4")

    btn = QtWidgets.QPushButton(parent=w)
    btn.setText("Push Me")
    btn.setIcon(QtGui.QIcon("internet-icon.png"))
    lbl = QtWidgets.QLabel(parent=w)
    lbl.setText("Look at Me")

    hbox = QtWidgets.QHBoxLayout()
    hbox.addStretch()
    hbox.addWidget(lbl)
    hbox.addStretch()

    vbox = QtWidgets.QVBoxLayout()
    vbox.addWidget(btn)
    vbox.addLayout(hbox)
    w.setLayout(vbox)

    w.show()
    sys.exit(app.exec_())


window()

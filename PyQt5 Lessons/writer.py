import os
import sys
from PyQt5.QtWidgets import (
    QApplication, QWidget, QTextEdit, QPushButton, QVBoxLayout, QHBoxLayout, QFileDialog)


class Notepad(QWidget):

    def __init__(self):
        super(Notepad, self).__init__()
        self.text = QTextEdit(self)
        self.clear_button = QPushButton("Clear")
        self.save_button = QPushButton("Save")
        self.open_button = QPushButton("Open")

        self.init_ui()

    def init_ui(self):
        vbox_layout = QVBoxLayout()
        hbox_layout = QHBoxLayout()

        hbox_layout.addWidget(self.clear_button)
        hbox_layout.addWidget(self.save_button)

        hbox_layout.addWidget(self.open_button)
        vbox_layout.addWidget(self.text)
        vbox_layout.addLayout(hbox_layout)

        self.clear_button.clicked.connect(self.clear_text)
        self.open_button.clicked.connect(self.open_textfile)
        self.save_button.clicked.connect(self.save_text)

        self.setLayout(vbox_layout)
        self.setWindowTitle("PyQt5 TextEdit")

        self.show()

    def save_text(self):
        """ Use a window dialog to navigate to a destination folder.
            Then save the file.
        """
        curr_dir = os.path.dirname(os.path.abspath(__file__))
        filename = QFileDialog.getSaveFileName(self, "Save File", curr_dir)

        with open(filename[0], "w") as fhandle:
            my_text = self.text.toPlainText()
            fhandle.write(my_text)

    def clear_text(self):
        self.text.clear()

    def open_textfile(self):
        """ Use a window dialog to navigate to a target folder.
            Then open the selected file.
        """
        curr_dir = os.path.dirname(os.path.abspath(__file__))
        filename = QFileDialog.getOpenFileName(self, "Save File", curr_dir)

        with open(filename[0], "r") as fhandle:
            file_text = fhandle.read()
            self.text.setText(file_text)


# Setup event loop
app = QApplication(sys.argv)
writer = Notepad()
sys.exit(app.exec_())

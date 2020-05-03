import sys
from PyQt5.QtWidgets import (
    QApplication, QWidget, QTextEdit, QPushButton, QVBoxLayout)


class Notepad(QWidget):

    def __init__(self):
        super(Notepad, self).__init__()
        self.text = QTextEdit(self)
        self.clear_button = QPushButton("Save")

        self.init_ui()

    def init_ui(self):
        layout = QVBoxLayout()
        layout.addWidget(self.text)
        layout.addWidget(self.clear_button)

        self.clear_button.clicked.connect(self.save_text)

        self.setLayout(layout)
        self.setWindowTitle("PyQt5 TextEdit")

        self.show()

    def save_text(self):
        import os

        curr_dir = os.path.dirname(os.path.abspath(__file__))
        output_file = os.path.join(curr_dir, "Resources", "test.txt")

        with open(output_file, "w") as fhandle:
            my_text = self.text.toPlainText()
            fhandle.write(my_text)


# Setup event loop
app = QApplication(sys.argv)
writer = Notepad()
sys.exit(app.exec_())

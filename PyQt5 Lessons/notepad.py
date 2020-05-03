import os
import sys
from PyQt5.QtWidgets import (
    QApplication, QWidget, QTextEdit, QPushButton, QVBoxLayout,
    QHBoxLayout, QFileDialog, QMainWindow, qApp, QAction, QMenu)

"""
    This application works like the Notepad application found in Microsoft
    Windows OSes. The Editor class contains a QTextEdit, QPushButtons, and
    QBoxLayouts. It also has member methods, which serve as slots for signalling
    widgets.
"""


class Editor(QWidget):

    def __init__(self):
        super(Editor, self).__init__()
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

        if not filename[0]:
            return

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

        if not filename[0]:
            return

        with open(filename[0], "r") as fhandle:
            file_text = fhandle.read()
            self.text.setText(file_text)


class Notepad(QMainWindow):

    def __init__(self):
        super().__init__()

        self.form_widget = Editor()
        self.setCentralWidget(self.form_widget)

        self.init_ui()

    def init_ui(self):

        # Create Menu Bar
        menu_bar = self.menuBar()

        # Create Root Menus
        file_menu = menu_bar.addMenu("File")
        edit_menu = menu_bar.addMenu("Edit")

        # Create Actions for Menus
        new_action = QAction("&New", self)
        new_action.setShortcut("Ctrl+N")

        open_action = QAction("&Open", self)
        open_action.setShortcut("Ctrl+O")

        save_action = QAction("&Save", self)
        save_action.setShortcut("Ctrl+S")

        exit_action = QAction("E&xit", self)
        exit_action.setShortcut("Ctrl+X")

        find_action = QAction("Find...", self)
        replace_action = QAction("Replace...", self)

        # Add actions to Menus
        file_menu.addAction(new_action)
        file_menu.addAction(open_action)
        file_menu.addAction(save_action)
        file_menu.addAction(exit_action)

        find_menu = edit_menu.addMenu("Find")
        find_menu.addAction(find_action)
        find_menu.addAction(replace_action)

        # Events
        exit_action.triggered.connect(self.exit_trigger)
        file_menu.triggered.connect(self.respond)

        # Window settings
        self.setWindowTitle("My Menus")
        self.resize(600, 400)

        self.show()

    def exit_trigger(self):
        qApp.quit()

    def respond(self, menu: QAction):
        signal = menu.text()

        if signal == "&New":
            self.form_widget.clear_text()
        elif signal == "&Open":
            self.form_widget.open_textfile()
        elif signal == "&Save":
            self.form_widget.save_text()


# Setup event loop
app = QApplication(sys.argv)
editor = Notepad()
sys.exit(app.exec_())

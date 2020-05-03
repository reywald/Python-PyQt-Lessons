import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, qApp, QAction


class MenuDemos(QMainWindow):

    def __init__(self):
        super().__init__()

        # Create Menu Bar
        menu_bar = self.menuBar()

        # Create Root Menus
        file_menu = menu_bar.addMenu("File")
        edit_menu = menu_bar.addMenu("Edit")

        # Create Actions for Menus
        save_action = QAction("Save", self)
        save_action.setShortcut("Ctrl+S")

        new_action = QAction("New", self)
        new_action.setShortcut("Ctrl+N")

        exit_action = QAction("E&xit", self)
        exit_action.setShortcut("Ctrl+X")

        find_action = QAction("Find...", self)
        replace_action = QAction("Replace...", self)

        # Add actions to Menus
        file_menu.addAction(new_action)
        file_menu.addAction(save_action)
        file_menu.addAction(exit_action)

        find_menu = edit_menu.addMenu("Find")
        find_menu.addAction(find_action)
        find_menu.addAction(replace_action)

        # Events
        exit_action.triggered.connect(self.exit_trigger)

        self.setWindowTitle("My Menus")
        self.resize(600, 400)

        self.show()

    def exit_trigger(self):
        qApp.quit()

    def selected(self):
        pass


app = QApplication(sys.argv)
menus = MenuDemos()
sys.exit(app.exec_())

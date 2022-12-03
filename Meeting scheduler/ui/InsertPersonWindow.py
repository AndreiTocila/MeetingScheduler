from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from database import SqlOperation
import ui


def do_insert(name: str, surname: str):
    """
        This method is used to insert a person into database.

        :return: None
    """
    SqlOperation.insert_person(name, surname)


class InsertPersonWindow(QMainWindow):
    """
      This class is used to create the insert person window.
    """

    def __init__(self):
        super(InsertPersonWindow, self).__init__()
        self.main_window = None
        self.init_window()

    def init_window(self):
        """
            This method is used to initialize the window.

            :return: None
        """
        self.setFixedSize(800, 800)
        self.setWindowTitle("Meeting scheduler")
        self.init_ui()
        self.show()

    def init_ui(self):
        """
            This method is used to initialize the user interface.

            :return: None
        """
        name_label = QLabel("Name", self)
        name_label.setGeometry(120, 100, 400, 100)
        name_label.setFont(QFont('Times', 15))

        surname_label = QLabel("Surname", self)
        surname_label.setGeometry(120, 200, 400, 100)
        surname_label.setFont(QFont('Times', 15))

        name_line = QLineEdit(self)
        name_line.setGeometry(240, 125, 400, 50)
        name_line.setFont(QFont('Times', 12))

        surname_line = QLineEdit(self)
        surname_line.setGeometry(240, 225, 400, 50)
        surname_line.setFont(QFont('Times', 12))

        insert_person_button = QPushButton("Insert new person", self)
        insert_person_button.setGeometry(200, 400, 400, 100)
        insert_person_button.setFont(QFont('Times', 15))
        insert_person_button.clicked.connect(lambda: do_insert(name_line.text(), surname_line.text()))

        back_button = QPushButton("Back", self)
        back_button.setGeometry(25, 725, 100, 50)
        back_button.setFont(QFont('Times', 15))
        back_button.clicked.connect(self.go_to_main_window)

    def go_to_main_window(self):
        """
            This method is used to go to the main window.

            :return: None
        """
        self.main_window = ui.MainWindow()
        self.hide()

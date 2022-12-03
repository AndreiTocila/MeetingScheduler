import re

from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
import ui
from service import MeetingService


def do_insert(start_date: str, end_date: str, participants: str):
    """
    This method is used to insert a meeting into the database.

    :param start_date: start date of the meeting
    :param end_date: end date of the meeting
    :param participants: list of participants

    :return: None
    """
    participants_list = []
    for person in re.split(r',\s*', participants):
        name, surname = person.split(" ")
        participants_list.append((name, surname))
    MeetingService.insert_meeting(start_date, end_date, participants_list)


class InsertMeetingWindow(QMainWindow):
    """
        This method is used to create the insert meeting window.
    """

    def __init__(self):
        super(InsertMeetingWindow, self).__init__()
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
            This method is used to initialize the user interface and connect the buttons to the methods.

            :return: None
        """
        start_date_label = QLabel("Start date", self)
        start_date_label.setGeometry(145, 120, 110, 100)
        start_date_label.setFont(QFont('Times', 15))

        start_date_input = QDateTimeEdit(self)
        start_date_input.setGeometry(50, 200, 300, 100)
        start_date_input.setFont(QFont('Times', 12))

        end_date_label = QLabel("End date", self)
        end_date_label.setGeometry(545, 120, 110, 100)
        end_date_label.setFont(QFont('Times', 15))

        end_date_input = QDateTimeEdit(self)
        end_date_input.setGeometry(450, 200, 300, 100)
        end_date_input.setFont(QFont('Times', 12))

        participants_label = QLabel("Participants", self)
        participants_label.setGeometry(335, 320, 130, 100)
        participants_label.setFont(QFont('Times', 15))

        participants_input = QLineEdit(self)
        participants_input.setGeometry(25, 390, 750, 50)
        participants_input.setFont(QFont('Times', 12))

        insert_meeting_button = QPushButton("Insert new meeting", self)
        insert_meeting_button.setGeometry(200, 500, 400, 100)
        insert_meeting_button.setFont(QFont('Times', 15))
        insert_meeting_button.clicked.connect(
            lambda: do_insert(start_date_input.dateTime().toString("yyyy-MM-dd hh:mm"),
                              end_date_input.dateTime().toString("yyyy-MM-dd hh:mm"),
                              participants_input.text()))

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

from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from .InsertPersonWindow import InsertPersonWindow
from .InsertMeetingWindow import InsertMeetingWindow


class MainWindow(QMainWindow):
    """
      This class is used to create the main window.
    """

    def __init__(self):
        super(MainWindow, self).__init__()
        self.insert_person_window = None
        self.insert_meeting_window = None
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
        insert_person_button = QPushButton("Insert new person", self)
        insert_meeting_button = QPushButton("Insert new meeting", self)
        show_meetings_button = QPushButton("Show meetings between interval", self)
        export_button = QPushButton("Export", self)

        insert_person_button.setGeometry(200, 100, 400, 100)
        insert_meeting_button.setGeometry(200, 250, 400, 100)
        show_meetings_button.setGeometry(200, 400, 400, 100)
        export_button.setGeometry(200, 550, 400, 100)

        insert_person_button.setFont(QFont('Times', 15))
        insert_meeting_button.setFont(QFont('Times', 15))
        show_meetings_button.setFont(QFont('Times', 15))
        export_button.setFont(QFont('Times', 15))

        insert_person_button.clicked.connect(self.goto_to_insert_person)
        insert_meeting_button.clicked.connect(self.goto_to_insert_meeting)

    def goto_to_insert_person(self):
        """
            This method is used to go to the insert person window.

            :return: None
        """
        self.insert_person_window = InsertPersonWindow()
        self.hide()

    def goto_to_insert_meeting(self):
        """
            This method is used to go to the insert meeting window.

            :return: None
        """
        self.insert_meeting_window = InsertMeetingWindow()
        self.hide()

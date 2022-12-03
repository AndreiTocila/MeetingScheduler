from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
import ui
from database import SqlOperation


def do_show_meetings(start_date: str, end_date: str):
    """
    This method is used to show the meetings between two dates.

    :param start_date: start date
    :param end_date: end date

    :return: None
    """
    meetings = SqlOperation.select_interval_meetings(start_date, end_date)
    if len(meetings) == 0:
        print("No meetings found.")
    else:
        for key, value in meetings.items():
            start_date, end_date = key.split(" - ")
            print("--------------------")
            print("Start date: %s" % start_date)
            print("End date: %s" % end_date)
            print("Participants: %s" % ", ".join(value))
            print("--------------------")


class ShowMeetingsWindow(QMainWindow):
    """
        This method is used to show the meetings.
    """

    def __init__(self):
        super(ShowMeetingsWindow, self).__init__()
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

        show_meetings_button = QPushButton("Show meetings", self)
        show_meetings_button.setGeometry(200, 390, 400, 100)
        show_meetings_button.setFont(QFont('Times', 15))
        show_meetings_button.clicked.connect(
            lambda: do_show_meetings(start_date_input.dateTime().toString("yyyy-MM-dd hh:mm"),
                                     end_date_input.dateTime().toString("yyyy-MM-dd hh:mm")))

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

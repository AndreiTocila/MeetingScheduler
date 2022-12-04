from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from utils import MyCalendar
import ui


class ExportImportWindow(QMainWindow):
    """
      This class is used to create the export/import window.
    """

    def __init__(self):
        super(ExportImportWindow, self).__init__()
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
        export_button = QPushButton("Export", self)
        export_button.setGeometry(200, 250, 400, 100)
        export_button.setFont(QFont('Times', 15))
        export_button.clicked.connect(lambda: MyCalendar.export_calendar())

        import_button = QPushButton("Import", self)
        import_button.setGeometry(200, 400, 400, 100)
        import_button.setFont(QFont('Times', 15))
        import_button.clicked.connect(lambda: self.import_calendar())

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

    def import_calendar(self):
        """
            This method is used to import a calendar.

            :return: None
        """
        fname = QFileDialog.getOpenFileName(self, "Open file", "calendars", "ICalendar (*.ics)")
        if fname[0]:
            MyCalendar.import_calendar(fname[0])


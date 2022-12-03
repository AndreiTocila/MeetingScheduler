from ui import MainWindow
from PyQt5.QtWidgets import QApplication
import sys

app = QApplication(sys.argv)
win = MainWindow()
sys.exit(app.exec_())

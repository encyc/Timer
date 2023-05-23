from PyQt5 import QtCore, QtGui, QtWidgets
from Dialog import *
import sys

if __name__ == "__main__":
    app = QApplication(sys.argv)
    widgets = QtWidgets.QMainWindow()
    timer_app = TimerApp(NoteManager())
    timer_app.setup_ui(widgets)
    widgets.show()

    sys.exit(app.exec_())

from NoteManager import *
from Dialog import *
import sys

if __name__ == "__main__":
    app = QApplication(sys.argv)

    timer_app = TimerApp(NoteManager())
    timer_app.show()

    sys.exit(app.exec_())

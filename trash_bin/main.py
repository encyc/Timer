from TimerApp import *
from Note import *
from Alarm import *
from Reminder import *



if __name__ == "__main__":
    import sys

    app = QApplication(sys.argv)
    timer_app = TimerApp()
    timer_app.show()
    sys.exit(app.exec_())

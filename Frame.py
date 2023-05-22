from NoteManager import *
from AlarmManager import *
from Dialog import *
import sys

if __name__ == "__main__":
    app = QApplication(sys.argv)

    # 创建一个NoteManager对象并加载笔记
    note_manager = NoteManager()
    note_manager.load_notes()

    timer_app = TimerApp(NoteManager())
    timer_app.show()

    sys.exit(app.exec_())

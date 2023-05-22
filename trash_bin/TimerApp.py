from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, QLabel, QPushButton, \
    QListWidget, QListWidgetItem, QDialog, QLineEdit, QVBoxLayout, QHBoxLayout, QTimeEdit, QMessageBox, QPlainTextEdit
from PyQt5.QtCore import Qt, QTime
import sys
from Note import *
from Alarm import *


class AlarmSettingsDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("闹钟设置")
        self.setGeometry(200, 200, 300, 150)
        self.create_dialog_layout()

    def create_dialog_layout(self):
        layout = QVBoxLayout()

        time_label = QLabel("时间:")
        self.time_edit = QTimeEdit()
        self.time_edit.setDisplayFormat("hh:mm")

        save_button = QPushButton("保存")
        save_button.clicked.connect(self.accept)

        layout.addWidget(time_label)
        layout.addWidget(self.time_edit)
        layout.addWidget(save_button)

        self.setLayout(layout)

    def get_alarm_time(self):
        return self.time_edit.time().toString()


class MainWindow(QMainWindow):
    def __init__(self, note_manager, alarm):
        super().__init__()
        self.note_manager = note_manager
        self.alarm = alarm
        self.setWindowTitle("Timer")
        self.setGeometry(100, 100, 600, 400)
        self.create_main_layout()

    def create_main_layout(self):
        main_widget = QWidget()
        main_layout = QVBoxLayout()

        note_list = QListWidget()
        self.populate_note_list(note_list)  # 填充笔记列表
        alarm_list = QListWidget()
        self.populate_alarm_list(alarm_list)  # 填充闹钟列表

        add_note_button = QPushButton("添加笔记")
        add_note_button.clicked.connect(self.show_add_note_dialog)

        delete_note_button = QPushButton("删除笔记")
        delete_note_button.clicked.connect(self.delete_note)

        add_alarm_button = QPushButton("添加闹钟")
        add_alarm_button.clicked.connect(self.show_add_alarm_dialog)

        delete_alarm_button = QPushButton("删除闹钟")
        delete_alarm_button.clicked.connect(self.delete_alarm)

        main_layout.addWidget(note_list)
        main_layout.addWidget(add_note_button)
        main_layout.addWidget(delete_note_button)
        # main_layout.addWidget(alarm_list)
        # main_layout.addWidget(add_alarm_button)
        # main_layout.addWidget(delete_alarm_button)

        main_widget.setLayout(main_layout)
        self.setCentralWidget(main_widget)

    def populate_note_list(self, note_list):
        note_list.clear()
        for note in self.note_manager.notes:
            note_title = note.get('title')
            note_list.addItem(note_title)

    def populate_alarm_list(self, alarm_list):
        alarm_list.clear()
        alarms = self.alarm.get_alarms()
        for alarm in alarms:
            alarm_time = alarm.toString("hh:mm")
            alarm_list.addItem(alarm_time)

    def show_add_note_dialog(self):
        # 实现添加笔记的对话框
        pass

    def delete_note(self):
        # 实现删除笔记的逻辑
        pass

    def show_add_alarm_dialog(self):
        dialog = AlarmSettingsDialog(self)
        if dialog.exec_() == QDialog.Accepted:
            alarm_time = dialog.get_alarm_time()
            self.alarm.add_alarm(alarm_time)
            self.populate_alarm_list()

    def delete_alarm(self):
        selected_items = self.alarm_list.selectedItems()
        if len(selected_items) > 0:
            alarm_index = self.alarm_list.row(selected_items[0])
            confirm_dialog = QMessageBox.question(self, '确认删除', '确定要删除该闹钟吗？',
                                                  QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
            if confirm_dialog == QMessageBox.Yes:
                self.alarm.delete_alarm(alarm_index)
                self.populate_alarm_list()


if __name__ == "__main__":
    app = QApplication(sys.argv)

    # 创建一个NoteManager对象并加载笔记
    note_manager = NoteManager()
    note_manager.load_notes()

    # 创建一个Alarm对象
    alarm = Alarm()

    # 创建主窗口并显示
    main_window = MainWindow(note_manager, alarm)
    main_window.show()

    sys.exit(app.exec_())

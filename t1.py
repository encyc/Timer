from PyQt5.QtWidgets import QDialog, QLabel, QTimeEdit, QPushButton, QVBoxLayout, QListWidget, \
    QMainWindow, QWidget, QApplication
import json

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


class Alarm:
    def __init__(self):
        self.alarms = []

    def add_alarm(self, time):
        self.alarms.append(time)

    def delete_alarm(self, index):
        del self.alarms[index]

    def get_alarms(self):
        return self.alarms


class NoteManager:
    def __init__(self):
        self.notes_file = 'note_file.json'
        self.notes = []
        self.load_notes()

    def load_notes(self):
        # 从文件或数据库中加载保存的笔记列表
        # 将加载的笔记存储在self.notes列表中
        try:
            with open(self.notes_file, 'r') as f:
                self.notes = json.load(f)
        except FileNotFoundError:
            # 如果文件不存在，则不做任何操作
            pass

    def save_notes(self):
        # 将当前的笔记列表self.notes保存到文件或数据库中
        # 示例代码，这里不执行实际的保存操作
        with open(self.notes_file, 'w') as f:
            json.dump(self.notes, f, default=lambda x: x.__dict__)

    def add_note(self, title, content):
        # 创建一个新的笔记，并添加到self.notes列表中
        # 参数title为笔记标题，参数content为笔记内容
        note = {'title': title, 'content': content}
        self.notes.append(note)
        self.save_notes()  # 保存笔记列表

    def edit_note(self, index, title, content):
        # 编辑指定索引的笔记
        # 参数index为要编辑的笔记在self.notes列表中的索引
        # 参数title为笔记标题，参数content为笔记内容
        if index < len(self.notes):
            self.notes[index]['title'] = title
            self.notes[index]['content'] = content
            self.save_notes()  # 保存笔记列表

    def delete_note(self, index):
        # 删除指定索引的笔记
        # 参数index为要删除的笔记在self.notes列表中的索引
        if index < len(self.notes):
            del self.notes[index]
            self.save_notes()  # 保存笔记列表



class MainWindow(QMainWindow):
    def __init__(self, note_manager, alarm):
        super().__init__()
        self.note_manager = note_manager
        self.alarm = alarm
        self.setWindowTitle("Timer")
        self.setGeometry(200, 200, 400, 300)
        self.create_main_layout()

    def create_main_layout(self):
        main_widget = QWidget()
        main_layout = QVBoxLayout()

        note_list = QListWidget()
        self.populate_note_list(note_list)  # 填充笔记列表

        add_note_button = QPushButton("添加笔记")
        add_note_button.clicked.connect(self.show_add_note_dialog)

        main_layout.addWidget(note_list)
        main_layout.addWidget(add_note_button)

        main_widget.setLayout(main_layout)
        self.setCentralWidget(main_widget)

    def populate_note_list(self, note_list):
        note_list.clear()
        for note in self.note_manager.notes:
            note_title = note.get('title')
            note_list.addItem(note_title)

            alarm_button = QPushButton("闹钟")
            alarm_button.clicked.connect(self.show_alarm_settings_dialog)
            note_list.setItemWidget(note_list.item(note_list.count() - 1), alarm_button)

    def show_add_note_dialog(self):
        # 实现添加笔记的对话框
        pass

    def show_alarm_settings_dialog(self):
        dialog = AlarmSettingsDialog(self)
        if dialog.exec_() == QDialog.Accepted:
            alarm_time = dialog.get_alarm_time()
            self.alarm.add_alarm(alarm_time)

    def delete_note(self):
        # 实现删除笔记的逻辑
        pass


if __name__ == "__main__":
    app = QApplication([])

    # 创建一个NoteManager对象并加载笔记
    note_manager = NoteManager()
    note_manager.load_notes()

    # 创建一个Alarm对象
    alarm = Alarm()

    # 创建主窗口并显示
    main_window = MainWindow(note_manager, alarm)
    main_window.show()

    app.exec_()

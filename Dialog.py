from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, QLabel, QPushButton, \
    QListWidget, QListWidgetItem, QDialog, QLineEdit, QVBoxLayout, QHBoxLayout, QTimeEdit, QMessageBox, QPlainTextEdit
from PyQt5.QtCore import Qt, QTime




class TimerApp(QMainWindow):
    def __init__(self,note_manager):
        super().__init__()
        self.setWindowTitle("Timer")
        self.setGeometry(100, 100, 600, 400)
        self.note_manager = note_manager
        self.setup_ui()

    def setup_ui(self):
        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)

        self.note_list = QListWidget()
        self.populate_note_list(self.note_list)  # 填充笔记列表

        self.add_note_button = QPushButton("Add Note")
        self.delete_note_button = QPushButton("Delete Note")
        self.alarm_button = QPushButton("Alarms")

        self.add_note_button.clicked.connect(self.add_note)
        self.delete_note_button.clicked.connect(self.delete_note)
        self.alarm_button.clicked.connect(self.open_alarm_page)


        buttons_layout = QHBoxLayout()
        buttons_layout.addWidget(self.add_note_button)
        buttons_layout.addWidget(self.delete_note_button)
        buttons_layout.addWidget(self.alarm_button)

        layout = QVBoxLayout(self.central_widget)
        layout.addWidget(self.note_list)
        layout.addLayout(buttons_layout)


    def populate_note_list(self, note_list):
        note_list.clear()
        for note in self.note_manager.notes:
            note_title = note.get('title')
            note_list.addItem(note_title)


    def add_note(self):
        note_dialog = NoteDialog()
        note_manager = NoteManager()
        if note_dialog.exec_() == QDialog.Accepted:

            title_edit, content_edit = note_dialog.get_note()
            note_manager.add_note(title_edit, content_edit)
            #
            # self.note_list.append(note)
            # self.refresh_note_list()
            #
            # # Get the newly added note item
            # item = self.note_list.item(self.note_list.count() - 1)
            #
            # # Connect the item clicked event to open the alarm page
            # item.clicked.connect(lambda: self.open_alarm_page(note))

    def delete_note(self):
        selected_items = self.note_list.selectedItems()
        for item in selected_items:
            index = self.note_list.row(item)
            del self.notes[index]

        self.refresh_note_list()

    def open_alarm_page(self, note):
        alarm_page = AlarmPage(note.get_alarms())
        if alarm_page.exec_() == QDialog.Accepted:
            alarms = alarm_page.get_alarms()
            note.set_alarms(alarms)

    def refresh_note_list(self):
        self.note_list.clear()
        for note in self.notes:
            item = QListWidgetItem(note.get_title())
            item.setFlags(item.flags() | Qt.ItemIsEditable)
            self.note_list.addItem(item)

            # Add alarm icon
            alarm_icon = QLabel()
            alarm_icon.setPixmap(
                QApplication.style().standardIcon(QApplication.IconMode.Computer).pixmap(16, 16))
            self.note_list.setItemWidget(item, alarm_icon)

    def closeEvent(self, event):
        reply = QMessageBox.question(self, "Quit", "Are you sure you want to quit?", QMessageBox.Yes | QMessageBox.No,
                                     QMessageBox.No)
        if reply == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()


class NoteDialog(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Add Note")

        self.title_label = QLabel("Title:")
        self.title_edit = QLineEdit()
        self.content_label = QLabel("Content:")
        self.content_edit = QPlainTextEdit()
        self.save_button = QPushButton("Save")
        self.cancel_button = QPushButton("Cancel")

        layout = QVBoxLayout(self)
        layout.addWidget(self.title_label)
        layout.addWidget(self.title_edit)
        layout.addWidget(self.content_label)
        layout.addWidget(self.content_edit)
        layout.addWidget(self.save_button)
        layout.addWidget(self.cancel_button)

        self.save_button.clicked.connect(self.accept)
        self.cancel_button.clicked.connect(self.reject)

        self.nm = NoteManager()

    def get_note(self):
        title_edit = self.title_edit
        content_edit = self.content_edit
        # note = {'title:' self.title_edit, 'content':self.content_edit}
        # set_title(self.title_edit.text())
        # set_content(self.content_edit.toPlainText())
        return title_edit, content_edit




class AlarmPage(QDialog):
    def __init__(self, alarms):
        super().__init__()
        self.setWindowTitle("Alarms")

        self.alarms = alarms

        self.alarm_list = QListWidget()
        self.add_alarm_button = QPushButton("Add Alarm")
        self.delete_alarm_button = QPushButton("Delete Alarm")
        self.save_button = QPushButton("Save")
        self.cancel_button = QPushButton("Cancel")

        buttons_layout = QHBoxLayout()
        buttons_layout.addWidget(self.add_alarm_button)
        buttons_layout.addWidget(self.delete_alarm_button)
        buttons_layout.addWidget(self.save_button)
        buttons_layout.addWidget(self.cancel_button)

        layout = QVBoxLayout(self)
        layout.addWidget(self.alarm_list)
        layout.addLayout(buttons_layout)

        self.add_alarm_button.clicked.connect(self.add_alarm)
        self.delete_alarm_button.clicked.connect(self.delete_alarm)
        self.save_button.clicked.connect(self.accept)
        self.cancel_button.clicked.connect(self.reject)

        self.refresh_alarm_list()

    def add_alarm(self):
        alarm_dialog = AlarmDialog()
        if alarm_dialog.exec_() == QDialog.Accepted:
            alarm = alarm_dialog.get_alarm()
            self.alarms.append(alarm)
            self.refresh_alarm_list()

    def delete_alarm(self):
        selected_items = self.alarm_list.selectedItems()
        for item in selected_items:
            index = self.alarm_list.row(item)
            del self.alarms[index]

        self.refresh_alarm_list()

    def get_alarms(self):
        return self.alarms

    def refresh_alarm_list(self):
        self.alarm_list.clear()
        for alarm in self.alarms:
            item = QListWidgetItem(alarm.get_info())
            item.setFlags(item.flags() | Qt.ItemIsEditable)
            self.alarm_list.addItem(item)


class AlarmDialog(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Add Alarm")

        self.name_label = QLabel("Name:")
        self.name_edit = QLineEdit()
        self.time_label = QLabel("Time:")
        self.time_edit = QTimeEdit()
        self.repeat_label = QLabel("Repeat:")
        self.repeat_edit = QLineEdit()
        self.sound_label = QLabel("Sound:")
        self.sound_edit = QLineEdit()
        self.save_button = QPushButton("Save")
        self.cancel_button = QPushButton("Cancel")

        layout = QVBoxLayout(self)
        layout.addWidget(self.name_label)
        layout.addWidget(self.name_edit)
        layout.addWidget(self.time_label)
        layout.addWidget(self.time_edit)
        layout.addWidget(self.repeat_label)
        layout.addWidget(self.repeat_edit)
        layout.addWidget(self.sound_label)
        layout.addWidget(self.sound_edit)
        layout.addWidget(self.save_button)
        layout.addWidget(self.cancel_button)

        self.save_button.clicked.connect(self.accept)
        self.cancel_button.clicked.connect(self.reject)

    def get_alarm(self):
        name = self.name_edit.text()
        time = self.time_edit.time()
        repeat = self.repeat_edit.text()
        sound = self.sound_edit.text()

        alarm = Alarm(name, time, repeat, sound)
        return alarm

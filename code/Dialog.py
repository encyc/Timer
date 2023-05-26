from PyQt5.QtWidgets import QApplication, QMainWindow, QTableWidgetItem, QWidget, QVBoxLayout, QHBoxLayout, QLabel, QPushButton, \
    QListWidget, QListWidgetItem, QDialog, QLineEdit, QVBoxLayout, QHBoxLayout, QTimeEdit, QMessageBox, QPlainTextEdit, QHeaderView
from PyQt5.QtCore import Qt, QTime
from PyQt5 import QtCore, QtGui, QtWidgets
from NoteManager import *
from AlarmManager import *

class TimerApp(QMainWindow):
    def __init__(self):
        super().__init__()
        # 设置Timer主窗口
        self.setWindowTitle("Timer")
        self.setGeometry(100, 100, 600, 400)
        # 初始化NoteManager类
        self.note_manager = NoteManager()
        self.note_list = None
        # 初始化AlarmManger类
        self.alarm_manager = AlarmManager()
        self.alarm_list = None

    def get_note_list(self):
        self.note_manager.load_notes()
        note_list = self.note_manager.notes
        for i in range(len(note_list)):
            item = note_list[i]
            row = self.tableWidget.rowCount()
            self.tableWidget.insertRow(row)
            for j in range(len(item)):
                item = QTableWidgetItem(str(note_list[i][j]))
                self.tableWidget.setItem(row, j, item)


    def setup_ui(self, MainWindow):
        # MainWindow
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(20, 40, 751, 461))

        # sizePolicy
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tableWidget.sizePolicy().hasHeightForWidth())

        # tableWidget
        self.tableWidget.setSizePolicy(sizePolicy)
        self.tableWidget.setMouseTracking(False)
        self.tableWidget.setTabletTracking(False)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(4)
        self.tableWidget.setRowCount(0)

        self.tableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)

        # item
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)
        self.verticalScrollBar = QtWidgets.QScrollBar(self.centralwidget)

        # 加载历史note信息
        self.get_note_list()

        # pushButton
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(20, 520, 241, 31))
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.add_note)

        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(280, 520, 241, 31))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_2.clicked.connect(self.on_delete_button_clicked)

        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(540, 520, 231, 31))
        self.pushButton_3.setObjectName("pushButton_3")
        # self.pushButton_3.clicked.connect(self.open_alarm_page)

        # munubar
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 23))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)

        # statusbar
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))

        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Note"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Subscribe"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Timer"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Status"))
        self.pushButton.setText(_translate("MainWindow", "Add Note"))
        self.pushButton_2.setText(_translate("MainWindow", "Delete Note"))

        # TODO:添加Setting界面内容
        self.pushButton_3.setText(_translate("MainWindow", "Setting"))

    # def populate_note_list(self, note_list):
    #     self.note_list.clear()
    #     self.note_manager.load_notes()
    #     for note in self.note_manager.notes:
    #         # note_title = note.get('title')
    #         note_title = note
    #         note_list.addItem(note_title)

    def refresh_note_list(self):
        self.tableWidget.clear()
        self.note_manager.load_notes()
        print(self.note_manager.notes)
        self.note_list = self.note_manager.notes
        row = self.tableWidget.rowCount()
        for i in range(len(self.note_list)):
            print(i)
            item = self.note_list[i]
            # row = self.tableWidget.rowCount()
            print(row,item )
            if i == row:
                self.tableWidget.insertRow(i)
            for j in range(len(item)):
                item = QTableWidgetItem(str(self.note_list[i][j]))
                self.tableWidget.setItem(i, j, item)


    def add_note(self):
        note_dialog = NoteDialog()
        if note_dialog.exec_() == QDialog.Accepted:
            title_edit, content_edit, datetime_edit = note_dialog.get_note()
            self.note_manager.add_note(title_edit, content_edit, datetime_edit)
            self.alarm_manager.set_alarm(title_edit,content_edit,datetime_edit,title_edit)
        # QApplication.processEvents()
        self.refresh_note_list()
        # self.get_note_list()


    def delete_note(self):
        selected_items = self.tableWidget.selectedItems()
        for item in selected_items:
            row = item.row()  # 获取选中文本所在的行
            column = item.column()  # 获取选中文本所在的列
            contents = item.text()  # 获取选中文本内容
            title = self.note_manager.notes[row][0]
            print("选择的内容为：", contents)
            print("所选的内容所在的行为：", row)
            print("所选的内容所在的列为：", column)

            self.note_manager.delete_note(row)
            self.alarm_manager.cancel_alarm(title)

            self.refresh_note_list()

    def on_delete_button_clicked(self):
        # 创建消息框
        msg_box = QMessageBox()
        msg_box.setIcon(QMessageBox.Question)
        msg_box.setText("Confirm?")
        msg_box.setWindowTitle("Delete Confirmation")
        msg_box.setStandardButtons(QMessageBox.Yes | QMessageBox.Cancel)
        msg_box.button(QMessageBox.Yes).setText('Delete')

        # 监听消息框里按钮的点击事件
        result = msg_box.exec_()
        if result == QMessageBox.Yes:
            # 用户选择了 "Delete" 按钮
            self.delete_note()
        else:
            # 用户选择了 "Cancel" 按钮，不做操作
            pass

    #
    # def refresh_note_list(self):
    #     # self.note_list.clear()
    #     self.note_list = self.note_manager.load_notes()
    #     print(self.note_list)
    #     self.populate_note_list(self.note_list)
    #         # # Add alarm icon
    #         # alarm_icon = QLabel()
    #         # alarm_icon.setPixmap(
    #         #     QApplication.style().standardIcon(QApplication.IconMode.Computer).pixmap(16, 16))
    #         # self.note_list.setItemWidget(item, alarm_icon)

    def closeEvent(self, event):
        reply = QMessageBox.question(self, "Quit", "See you my friend", QMessageBox.Yes | QMessageBox.No,
                                     QMessageBox.No)
        if reply == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()


from PyQt5.QtCore import Qt, QDateTime
from PyQt5.QtWidgets import QDialog, QLineEdit, QDateTimeEdit, QVBoxLayout, QFormLayout, QDialogButtonBox, QCheckBox, QSizePolicy


class NoteDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle('Add Note')

        # Create input boxes
        self.title_edit = QLineEdit()
        self.content_edit = QLineEdit()
        self.datetime_edit = QDateTimeEdit(QDateTime.currentDateTime())
        # self.datetime_edit.tostring("yyyy-MM-dd hh:mm:ss")
        # print(type(self.datetime_edit))

        # Create check box to show/hide date/time input box
        # self.show_datetime_check_box = QCheckBox('Set Alarm')
        # self.show_datetime_check_box.setChecked(True)
        # self.show_datetime_check_box.stateChanged.connect(self.on_show_datetime_state_changed)


        # Set content text box alignment to top-left
        self.content_edit.setAlignment(Qt.AlignTop | Qt.AlignLeft)

        # Set stretch factor for content text box to make it larger
        self.content_edit.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.content_edit.setMinimumHeight(100)


        # Create form layout and add input boxes
        form_layout = QFormLayout()
        form_layout.addRow('Title:', self.title_edit)
        form_layout.addRow('Content:', self.content_edit)


        # form_layout.addRow(self.show_datetime_check_box)
        # self.datetime_row_index = form_layout.rowCount()
        form_layout.addRow('Alarm:', self.datetime_edit)
        # self.datetime_edit.setVisible(True)

        # Create Save and Cancel buttons
        button_box = QDialogButtonBox(QDialogButtonBox.Save | QDialogButtonBox.Cancel)
        button_box.accepted.connect(self.accept)
        button_box.rejected.connect(self.reject)

        # Create vertical layout and add form layout and button box
        layout = QVBoxLayout()
        layout.addLayout(form_layout)
        layout.addWidget(button_box)

        # Set layout for QDialog
        self.setLayout(layout)

    def get_note(self):
        title_edit = self.title_edit.text()
        content_edit = self.content_edit.text()
        datetime_edit = self.datetime_edit.text()
        print(title_edit, content_edit, datetime_edit)
        # note = {'title:' self.title_edit, 'content':self.content_edit}
        # set_title(self.title_edit.text())
        # set_content(self.content_edit.toPlainText())
        return title_edit, content_edit, datetime_edit

    # def on_show_datetime_state_changed(self, state):
    #     self.datetime_edit.setVisible(state == Qt.Checked)
    #     self.layout().itemAt(self.datetime_row_index).widget().setVisible(state == Qt.Checked)


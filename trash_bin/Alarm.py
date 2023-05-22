from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, QLabel, QPushButton, \
    QListWidget, QListWidgetItem, QDialog, QLineEdit, QVBoxLayout, QHBoxLayout, QTimeEdit, QMessageBox, QPlainTextEdit
from PyQt5.QtCore import Qt, QTime
import sys
from Note import *


class Alarm:
    def __init__(self):
        self.alarms = []

    def add_alarm(self, time):
        self.alarms.append(time)

    def delete_alarm(self, index):
        del self.alarms[index]

    def get_alarms(self):
        return self.alarms
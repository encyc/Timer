from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QApplication, QMainWindow, QSystemTrayIcon, QMenu

class Example(QMainWindow):

    def __init__(self):
        super().__init__()

        # 初始化 QSystemTrayIcon 对象
        self.tray_icon = QSystemTrayIcon(self)
        self.tray_icon.setIcon(QIcon("icon.png"))
        self.tray_icon.setToolTip("Minimize to Tray")

        # 创建菜单
        menu = QMenu(self)
        action_open = menu.addAction("Open")
        action_exit = menu.addAction("Exit")
        self.tray_icon.setContextMenu(menu)

        # 信号槽连接
        action_exit.triggered.connect(qApp.quit)

        # 隐藏窗口
        self.setWindowFlags(Qt.WindowMinimizeButtonHint)
        self.hide()

        # 显示托盘图标
        self.tray_icon.show()

if __name__ == '__main__':
    app = QApplication([])
    ex = Example()
    app.exec_()

from PyQt5.QtWidgets import QApplication


class TimerApp(QMainWindow):
    def __init__(self, app):
        super().__init__()

        # 设置 Timer 主窗口
        self.setWindowTitle("Timer")
        self.setGeometry(100, 100, 600, 400)

        # ...

        # 信号槽连接
        action_exit.triggered.connect(app.quit)

        # 隐藏窗口
        self.setWindowFlags(Qt.WindowMinimizeButtonHint)
        self.hide()

        # 显示托盘图标
        self.tray_icon.show()
import ctypes

class Reminder:
    def __init__(self, name='', time='', content=''):
        self.name = name
        self.time = time
        self.content = content

    def set_name(self, name):
        self.name = name

    def set_time(self, time):
        self.time = time

    def set_content(self, content):
        self.content = content

    def get_name(self):
        return self.name

    def get_time(self):
        return self.time

    def get_content(self):
        return self.content

    def show_popup(self):
        ctypes.windll.user32.MessageBoxW(None, self.content, self.name, 0)



class AlarmManager:
    def __init__(self, name, time, repeat, sound):
        self.name = name
        self.time = time
        self.repeat = repeat
        self.sound = sound

    def set_name(self, name):
        self.name = name

    def get_name(self):
        return self.name

    def set_time(self, time):
        self.time = time

    def get_time(self):
        return self.time

    def set_repeat(self, repeat):
        self.repeat = repeat

    def get_repeat(self):
        return self.repeat

    def set_sound(self, sound):
        self.sound = sound

    def get_sound(self):
        return self.sound

    def get_info(self):
        return f"{self.name} - {self.time.toString('hh:mm')} - {self.repeat} - {self.sound}"

from datetime import datetime
import threading
from plyer import notification


class AlarmManager:
    def __init__(self):
        self.timer_threads = {}

    def set_alarm(self, title, message, date_time_str, alarm_id):
        date_time_obj = datetime.strptime(date_time_str, "%Y/%m/%d %H:%M")
        new_date_str = date_time_obj.strftime("%Y-%m-%d %H:%M:%S")
        new_date_obj = datetime.strptime(new_date_str, "%Y-%m-%d %H:%M:%S")
        time_diff = (new_date_obj - datetime.now()).total_seconds()
        print(time_diff)
        if time_diff <= 0:
            # print('过去已成往事')
            pass
        else:
            self.timer_threads[alarm_id] = threading.Timer(time_diff, self.on_alarm, args=[title, message])
            self.timer_threads[alarm_id].start()
            print('闹钟设置成功')
    # TODO:将duration转为参数化,在之后的setting menu里加上
    def on_alarm(self, title, message):
        notification.notify(title=title, message=message, timeout=120)

    def cancel_alarm(self, alarm_id):
        if alarm_id in self.timer_threads:
            timer_thread = self.timer_threads[alarm_id]
            timer_thread.cancel()
            del self.timer_threads[alarm_id]


# if __name__ == '__main__':
#     a = AlarmManager()
#
#     # 设置一个闹钟
#     a.set_alarm("提醒1", "该去休息了！", "2023/05/25 11:25", "alarm1")
#
#     # 在5秒后取消闹钟
#     timer = threading.Timer(5, a.cancel_alarm, args=["alarm1"])
#     timer.start()
#
#     # 设置另一个闹钟
#     a.set_alarm("提醒2", "该吃午饭了！", "2023/05/25 13:00", "alarm2")
#
#     # 在5秒后取消闹钟
#     timer2 = threading.Timer(5, a.cancel_alarm, args=["alarm2"])
#     timer2.start()
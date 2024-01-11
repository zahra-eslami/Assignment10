from datetime import datetime
import pytz

class Time:
    def __init__(self, hour, minute, second):
        self.hour = int(hour)
        self.minute =int(minute)
        self.second = int(second)

    def display(self):
        return f"{self.hour}:{self.minute}:{self.second}"

    def to_seconds(self):
        second=self.hour*3600+self.minute*60+self.second
        return second
    
    def change_local_time(self):
        current_time = datetime.now()
        second_timezone = pytz.timezone('America/New_York')
        second_time = current_time.astimezone(second_timezone).time()
        second_time=second_time.strftime("%H:%M:%S")
        return second_time

current_time = datetime.now()
formatted_time = current_time.strftime("%H:%M:%S")
 
time=formatted_time.split(":")
h=time[0]
m=time[1]
s=time[2]

time_1 = Time(h,m,s)
print("The Current Time is:", time_1.display())

total_seconds = time_1.to_seconds()
print("Convert time to secound :", total_seconds)

second_time=time_1.change_local_time()

print("Current time in Newyork is :", second_time)



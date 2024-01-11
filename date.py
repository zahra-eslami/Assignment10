from datetime import datetime
import calendar


class CustomDate:
    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day

    def display_date(self):
        return f"{self.year}-{self.month:02d}-{self.day:02d}"

    def day_of_week(self):
        day_index = datetime(self.year, self.month, self.day).weekday()
        days_of_week = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
        return days_of_week[day_index]

    def convert_to_shamsi(self):
        ...

current_date = datetime.now()
my_date = CustomDate(current_date.year, current_date.month, current_date.day)

print(f"Current Date: {my_date.display_date()}")
print(f"Current Day: {my_date.day_of_week()}")

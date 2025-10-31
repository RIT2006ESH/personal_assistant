import datetime

class TimeManager:
    def get_current_time(self):
        return datetime.datetime.now().strftime("%I:%M %p")

    def get_greeting(self):
        hour = datetime.datetime.now().hour
        if 0 <= hour < 12:
            return "Good Morning"
        elif 12 <= hour < 18:
            return "Good Afternoon"
        return "Good Evening"
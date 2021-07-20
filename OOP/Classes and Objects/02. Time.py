class Time:
    max_hours = 23
    max_minutes = 59
    max_seconds = 59

    def __init__(self, hours, minutes, seconds):
        self.hours = hours
        self.seconds = seconds
        self.minutes = minutes

    def set_time(self, hours, minutes, seconds):
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds

    def get_time(self):
        # def format_time(number):
        #     if number < 10:
        #         return f"0{number}"
        #     else:
        #         return f"{number}"
        #
        # return f"{format_time(self.hours)}:{format_time(self.minutes)}:{format_time(self.seconds)}"
        return f"{self.hours:02d}:{self.minutes:02d}:{self.seconds:02d}"

    def next_second(self):
        if self.seconds < Time.max_seconds:
            self.seconds += 1
        else:
            self.seconds = 0
            if self.minutes < Time.max_minutes:
                self.minutes += 1
            else:
                self.minutes = 0
                if self.hours < Time.max_hours:
                    self.hours += 1
                else:
                    self.hours = 0
        return self.get_time()


time = Time(9, 30, 59)
print(time.next_second())
time = Time(10, 59, 59)
print(time.next_second())
time = Time(23, 59, 59)
print(time.next_second())


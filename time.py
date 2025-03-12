class Time:
    max_hours = 23
    max_minutes = 59
    max_seconds = 59

    def __init__(self, hours, minutes, seconds):
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds

    def set_time(self, hours, minutes, seconds):
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds

    def get_time(self):
        return f"{self.hours:02d}:{self.minutes:02d}:{self.seconds:02d}"

    def next_second(self):

        #checks if seconds are to be set to zero or add another second
        if self.seconds + 1 > Time.max_seconds:
            self.seconds = 0
        else: self.seconds += 1

        #checks if minutes should be set to zero or add another minute
        if self.seconds == 0:
            if self.minutes + 1 > Time.max_minutes:
                self.minutes = 0
            else:
                self.minutes += 1

        #checks if another hour have passed
        if self.seconds == 0 and self.minutes == 0:
            if self.hours + 1 > Time.max_hours:
                self.hours = 0
            else:
                self.hours += 1

        return self.get_time()


'''
Creating a clock ticking with 1 sec forward. Time can be set through a method.
'''

time = Time(9, 30, 59)
print(time.next_second())
time = Time(10, 59, 59)
print(time.next_second())
time = Time(23, 59, 59)
print(time.next_second())




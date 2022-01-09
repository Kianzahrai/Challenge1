#Countdown Timer
import time

def countdown(time_second):
    while time_second:
        minutes, seconds = divmod(time_second, 60)
        timeformat = '{:02d}:{:02d} '.format(minutes, seconds)
        print(timeformat, end = '\r')
        time.sleep(1)
        time_second -= 1
    print("stop")
countdown(10)

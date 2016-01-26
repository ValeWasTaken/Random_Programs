# Python 3.4
import os
import time

def alarm_clock():
    wait = int(input('Sound alarm in how many seconds: '))
    time.sleep(wait)
    os.system("start C:/Users/Vale/Desktop/test.mp3")
alarm_clock()

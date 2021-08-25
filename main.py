from datetime import datetime
from time import sleep
import os

#TODO#1 - add option to set how many monitors probably imputing id's and saving it as json
#TODO#2 - add option to add custom time and resolutions
#TODO#3 - add a schedule and a way to display it


def isNowInTimePeriod(startTime, endTime, nowTime):  # this function is from stack overflow by the user rouble
    if startTime < endTime:
        return startTime <= nowTime <= endTime
    else:  # Over midnight
        return nowTime >= startTime or nowTime <= endTime


def TimeRezer(width, height, start, end, now, reznow):
    if isNowInTimePeriod(start, end, now):
        if reznow == f"{width}x{height}":
            pass
        else:
            print(f"your monitors will be changed to {width}x{height} until {end}")
            os.system(f"ChangeScreenResolution.exe /w={width} /h={height} /d=0")
            os.system(f"ChangeScreenResolution.exe /w={width} /h={height} /d=1")
            return f"{width}x{height}"


def TimeRezChanger(now, reznow):
    reznow = TimeRezer(1280, 720, "07:20", "08:07", now, reznow)  # 47 min
    reznow = TimeRezer(1366, 768, "08:08", "08:59", now, reznow)  # 51 min
    reznow = TimeRezer(1600, 900, "09:00", "11:19", now, reznow)  # 2 hours 19 min
    reznow = TimeRezer(1920, 1080, "11:20", "14:39", now, reznow)  # 3 hours 19 min
    reznow = TimeRezer(2560, 1440, "14:40", "07:19", now, reznow)  # 7 hours 21 min
    return reznow


CurrentRez = ""  # this has to exist I guess

print("Welcome to TTR or TimeToResolution\n" +
      "This program will change your resolution at specific time\n" +
      "for example at 07:20 your resolution will be set to 1280x720\n" +
      "and at 08:08 your resolution will be set to 1366x768 because 07:68, 68minutes is 1hour 8mins\n")
input("press any key to start")

while(True):
    DateTimeNow = datetime.now()
    TimeNow = DateTimeNow.strftime("%H:%M")
    print(TimeNow)
    CurrentRez = TimeRezChanger(TimeNow, CurrentRez)
    sleep(60)

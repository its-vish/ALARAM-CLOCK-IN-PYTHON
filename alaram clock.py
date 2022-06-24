import datetime
from signal import alarm
from playsound import playsound
alarm_hour=int(input("enter hour :"))
alarm_min=int(input("enter min :"))
alarm_am=input("am/pm:-")
if alarm_am=="pm":
    alarm_hour+=12
while True:
    if alarm_hour==datetime.datetime.now().hour and alarm_min==datetime.datetime.now().minute:
        print("playing sound using playsound")
        print("playing....")
        playsound('/home/navgurukul/Downloads/varsha ringtone')
        break

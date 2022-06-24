import os
import datetime
import time
c,b,a=input("Enter the date=").split("/")
hr,minn,sec=input(  "Enter the time=").split(":")
shedule_date=datetime.date(int(a),int(b),int(c))
n=1
while n>0:
    if time.localtime().tm_hour==int(hr) and time.localtime().tm_min==int(minn) and time.localtime().tm_sec==int(sec) and datetime.date.today()==shedule_date:
        os.startfile("/home/navgurukul/Downloads/varsha ringtone")
        break
    else:
        n+=1
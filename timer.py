import datetime
import sys
import platform

print()
print("****************")
print("Count down timer")
print("****************")
print()

print("Please type in a time to count down.")
print("Format = HH:MM:SS, range = 00:00:00 -> 23:59:59")
input_string = input(": ")

if not input_string.count(':') == 2:
    print("Invalid format.")
    sys.exit()

try:
    input_time = [int(tok) for tok in input_string.split(":")]
except:
    print("Invalid format.")
    sys.exit()

if str(input_time[0]).isnumeric() == False:
    print("HH needs to be a numeric number.")
    sys.exit()
elif int(input_time[0]) > 23:
    print("HH needs to be less than 24.")
    sys.exit()
else:
    hrs = int(input_time[0])

if str(input_time[1]).isnumeric() == False:
    print("MM needs to be a numeric number.")
    sys.exit()
elif int(input_time[1]) > 59:
    print("MM needs to be less than 60.")
    sys.exit()
else:
    mns = int(input_time[1])

if str(input_time[2]).isnumeric() == False:
    print("SS needs to be a numeric number.")
    sys.exit()
elif int(input_time[2]) > 59:
    print("SS needs to be less than 60.")
    sys.exit()
else:
    sec = int(input_time[2])

t1 = datetime.datetime.now()
t2 = t1 + datetime.timedelta(hours = hrs) + datetime.timedelta(minutes = mns) + datetime.timedelta(seconds = sec)
t3 = t2 - datetime.datetime.now()

if t3.seconds >= 0:
    print(str(t3)[:-7])

while datetime.datetime.now() < t2:
    t4 = t2 - datetime.datetime.now()
    if not t3.seconds == t4.seconds:
        t3 = t2 - datetime.datetime.now()
        print(str(t3)[:-7])

if platform.system() == "Windows":
    import winsound
    winsound.Beep(2000, 500)
else:
    import os
    os.system('afplay /System/Library/Sounds/Ping.aiff')


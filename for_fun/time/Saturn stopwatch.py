import time
from IPython.display import clear_output
print("The solar time model is used for this stopwatch. \n More info here: https://lco.global/spacebook/sky/sidereal-time/"
      " | https://science.nasa.gov/saturn/facts/ | \n https://en.wikipedia.org/wiki/Solar_time | https://en.wikipedia.org/wiki/Synodic_day")
ratio1 = ((10*60*60)+(14*60)) / (24*60*60)
ratio2 = ((10*60*60)+(38*60)+25.4) / (24*60*60)
ratio3 = ((10*60*60)+(39*60)+22.4) / (24*60*60)
ratioavg = (ratio1+ratio2+ratio3)/3
print(f'A day on Saturn lasts this many Earth days:\n'
      f'System I: {ratio1}\n'
      f'System II: {ratio2} (most common)\n'
      f'System III: {ratio3}')


def sys1():
    satu1day = 0
    while satu1day <= 365:
        satu1hour = 0
        while satu1hour < 24:
            satu1mins = 0
            while satu1mins < 60:
                satu1sec = 0
                while satu1sec < 60:
                    print(f"System I: {satu1day} : {satu1hour} : {satu1mins} : {satu1sec}", end='\x1b[2K')
                    time.sleep(ratio1)
                    clear_output()
                    satu1sec += 1
                satu1mins += 1
            satu1hour += 1
        satu1day += 1


def sys2():
    satu2day = 0
    while satu2day <= 365:
        satu2hour = 0
        while satu2hour < 24:
            satu2mins = 0
            while satu2mins < 60:
                satu2sec = 0
                while satu2sec < 60:
                    print(f"System II: {satu2day} : {satu2hour} : {satu2mins} : {satu2sec}", end='\x1b[2K')
                    time.sleep(ratio2)
                    clear_output()
                    satu2sec += 1
                satu2mins += 1
            satu2hour += 1
        satu2day += 1


def sys3():
    satu3day = 0
    while satu3day <= 365:
        satu3hour = 0
        while satu3hour < 24:
            satu3mins = 0
            while satu3mins < 60:
                satu3sec = 0
                while satu3sec < 60:
                    print(f"System III: {satu3day} : {satu3hour} : {satu3mins} : {satu3sec}", end='\x1b[2K')
                    time.sleep(ratio3)
                    clear_output()
                    satu3sec += 1
                satu3mins += 1
            satu3hour += 1
        satu3day += 1


inpsys = input("Pick a System for the stopwatch: 1, 2 or 3\n")
if inpsys == "1":
    sys1()
elif inpsys == "2":
    sys2()
elif inpsys == "3":
    sys3()
else:
    print("Wrong number!")

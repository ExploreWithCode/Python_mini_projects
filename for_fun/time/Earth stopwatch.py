import time
from IPython.display import clear_output
day = 0
while day <= 366:
    hour = 0
    while hour < 24:
        mins = 0
        while mins < 60:
            sec = 0
            while sec < 60:
                print(f"{day} : {hour} : {mins} : {sec}", end='\x1b[2K')
                time.sleep(0)
                clear_output()
                sec += 1
            mins += 1
        hour += 1
    day += 1

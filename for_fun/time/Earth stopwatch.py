import time
from IPython.display import clear_output
print("The solar time model is used for this stopwatch. \n More info here: https://lco.global/spacebook/sky/sidereal-time/ "
      "| https://en.wikipedia.org/wiki/Solar_time |\n https://en.wikipedia.org/wiki/Synodic_day")
day = 0
while day <= 366:
    hour = 0
    while hour < 24:
        mins = 0
        while mins < 60:
            sec = 0
            while sec < 60:
                print(f"Earth stopwatch: {day} : {hour} : {mins} : {sec}", end='\x1b[2K')
                time.sleep(1)
                clear_output()
                sec += 1
            mins += 1
        hour += 1
    day += 1

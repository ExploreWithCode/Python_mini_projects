import time
from IPython.display import clear_output
print("The solar time model is used for this stopwatch. \n More info here: https://lco.global/spacebook/sky/sidereal-time/ "
      "| https://en.wikipedia.org/wiki/Lunar_day | \n https://en.wikipedia.org/wiki/Solar_time | https://en.wikipedia.org/wiki/Synodic_day")
ratio = ((29*24*60*60)+(12*60*60)+(44*60)+2.9) / (24*60*60)
print(f'A day on Moon lasts {ratio} Earth days.')
day = 0
while day <= 365:
    moonhour = 0
    while moonhour < 24:
        moonmins = 0
        while moonmins < 60:
            moonsec = 0
            while moonsec < 60:
                print(f"Moon's stopwatch: {day} : {moonhour} : {moonmins} : {moonsec}", end='\x1b[2K')
                time.sleep(ratio)
                clear_output()
                moonsec += 1
            moonmins += 1
        moonhour += 1
    day += 1

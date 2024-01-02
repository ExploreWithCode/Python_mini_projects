import time
from IPython.display import clear_output
print("The solar time model is used for this stopwatch. \n More info here: https://lco.global/spacebook/sky/sidereal-time/"
      " | https://science.nasa.gov/jupiter/moons/himalia | \n https://en.wikipedia.org/wiki/Solar_time | https://en.wikipedia.org/wiki/Synodic_day")
ratio = (7.7819*60*60) / (24*60*60)
print(f"A day on Himalia, Jupiter's moon, lasts {ratio} Earth days.")
himday = 0
while himday <= 365:
    himhour = 0
    while himhour < 24:
        himmins = 0
        while himmins < 60:
            himsec = 0
            while himsec < 60:
                print(f"Himalia stopwatch: {himday} : {himhour} : {himmins} : {himsec}", end='\x1b[2K')
                time.sleep(ratio)
                clear_output()
                himsec += 1
            himmins += 1
        himhour += 1
    himday += 1
import time
from IPython.display import clear_output
print("The solar time model is used for this stopwatch. \n More info here: https://lco.global/spacebook/sky/sidereal-time/"
      " | https://science.nasa.gov/jupiter/moons/himalia | \n https://en.wikipedia.org/wiki/Solar_time | https://en.wikipedia.org/wiki/Synodic_day")
ratio = (7.7819*60*60) / (24*60*60)
print(f"A day on Himalia, Jupiter's moon, lasts {ratio} Earth days.")
himday = 0
while himday <= 365:
    himhour = 0
    while himhour < 24:
        himmins = 0
        while himmins < 60:
            himsec = 0
            while himsec < 60:
                print(f"Himalia stopwatch: {himday} : {himhour} : {himmins} : {himsec}", end='\x1b[2K')
                time.sleep(ratio)
                clear_output()
                himsec += 1
            himmins += 1
        himhour += 1
    himday += 1

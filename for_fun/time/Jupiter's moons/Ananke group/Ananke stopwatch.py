import time
from IPython.display import clear_output
print("The solar time model is used for this stopwatch. \n More info here: https://lco.global/spacebook/sky/sidereal-time/"
      " | https://science.nasa.gov/jupiter/moons/ananke | \n https://en.wikipedia.org/wiki/Solar_time | https://en.wikipedia.org/wiki/Synodic_day")
ratio = (8.31*60*60) / (24*60*60)
print(f"A day on Ananke, Jupiter's moon, lasts {ratio} Earth days.")
anankeday = 0
while anankeday <= 365:
    anankehour = 0
    while anankehour < 24:
        anankemins = 0
        while anankemins < 60:
            anankesec = 0
            while anankesec < 60:
                print(f"Ananke stopwatch: {anankeday} : {anankehour} : {anankemins} : {anankesec}", end='\x1b[2K')
                time.sleep(ratio)
                clear_output()
                anankesec += 1
            anankemins += 1
        anankehour += 1
    anankeday += 1

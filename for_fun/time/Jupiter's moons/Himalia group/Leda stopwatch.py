import time
from IPython.display import clear_output
print("The solar time model is used for this stopwatch. \n More info here: https://lco.global/spacebook/sky/sidereal-time/"
      " | https://science.nasa.gov/jupiter/moons/leda | \n https://en.wikipedia.org/wiki/Solar_time | https://en.wikipedia.org/wiki/Synodic_day")
ratio = (12.84*60*60) / (24*60*60)
print(f"A day on Leda, Jupiter's moon, lasts {ratio} Earth days.")
ledaday = 0
while ledaday <= 365:
    ledahour = 0
    while ledahour < 24:
        ledamins = 0
        while ledamins < 60:
            ledasec = 0
            while ledasec < 60:
                print(f"Leda stopwatch: {ledaday} : {ledahour} : {ledamins} : {ledasec}", end='\x1b[2K')
                time.sleep(ratio)
                clear_output()
                ledasec += 1
            ledamins += 1
        ledahour += 1
    ledaday += 1

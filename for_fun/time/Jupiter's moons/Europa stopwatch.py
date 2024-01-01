import time
from IPython.display import clear_output
print("The solar time model is used for this stopwatch. \n More info here: https://lco.global/spacebook/sky/sidereal-time/"
      " | https://science.nasa.gov/jupiter/moons/europa/facts/ | \n https://en.wikipedia.org/wiki/Solar_time | https://en.wikipedia.org/wiki/Synodic_day")
ratio = 3.551181
print(f"A day on Europa, Jupiter's moon, lasts {ratio} Earth days.")
europaday = 0
while europaday <= 365:
    europahour = 0
    while europahour < 24:
        europamins = 0
        while europamins < 60:
            europasec = 0
            while europasec < 60:
                print(f"Europa stopwatch: {europaday} : {europahour} : {europamins} : {europasec}", end='\x1b[2K')
                time.sleep(ratio)
                clear_output()
                europasec += 1
            europamins += 1
        europahour += 1
    europaday += 1

import time
from IPython.display import clear_output
print("The solar time model is used for this stopwatch. \n More info here: https://lco.global/spacebook/sky/sidereal-time/"
      " | https://science.nasa.gov/saturn/moons/hati / | \n https://en.wikipedia.org/wiki/Solar_time | https://en.wikipedia.org/wiki/Synodic_day")
ratio = 5.45 / 24
print(f"A day on Hati, Saturn's moon lasts {round(ratio, 7)} Earth days.")
hatiday = 0
while hatiday <= 365:
    hatihour = 0
    while hatihour < 24:
        hatimins = 0
        while hatimins < 60:
            hatisec = 0
            while hatisec < 60:
                print(f"Hati stopwatch: {hatiday} : {hatihour} : {hatimins} : {hatisec}", end='\x1b[2K')
                time.sleep(ratio)
                clear_output()
                hatisec += 1
            hatimins += 1
        hatihour += 1
    hatiday += 1

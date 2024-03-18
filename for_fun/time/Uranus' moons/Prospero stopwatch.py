import time
from IPython.display import clear_output
print("The solar time model is used for this stopwatch. \n More info here: https://lco.global/spacebook/sky/sidereal-time/"
      " | https://science.nasa.gov/uranus/moons/prospero/ | \n https://en.wikipedia.org/wiki/Solar_time | https://en.wikipedia.org/wiki/Synodic_day")
ratio = 7.145 / 24
print(f"A day on Prospero, Uranus' moon lasts {round(ratio, 8)} Earth days.")
prosperoday = 0
while prosperoday <= 365:
    prosperohour = 0
    while prosperohour < 24:
        prosperomins = 0
        while prosperomins < 60:
            prosperosec = 0
            while prosperosec < 60:
                print(f"Prospero stopwatch: {prosperoday} : {prosperohour} : {prosperomins} : {prosperosec}", end='\x1b[2K')
                time.sleep(ratio)
                clear_output()
                prosperosec += 1
            prosperomins += 1
        prosperohour += 1
    prosperoday += 1

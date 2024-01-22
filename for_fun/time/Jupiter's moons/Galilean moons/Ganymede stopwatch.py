import time
from IPython.display import clear_output
print("The solar time model is used for this stopwatch. \n More info here: https://lco.global/spacebook/sky/sidereal-time/"
      " | https://science.nasa.gov/jupiter/moons/ganymede/facts/ | \n https://en.wikipedia.org/wiki/Solar_time | https://en.wikipedia.org/wiki/Synodic_day")
ratio = 7.15455296
print(f"A day on Ganymede, Jupiter's moon, lasts {ratio} Earth days.")
ganday = 0
while ganday <= 365:
    ganhour = 0
    while ganhour < 24:
        ganmins = 0
        while ganmins < 60:
            gansec = 0
            while gansec < 60:
                print(f"Ganymede stopwatch: {ganday} : {ganhour} : {ganmins} : {gansec}", end='\x1b[2K')
                time.sleep(ratio)
                clear_output()
                gansec += 1
            ganmins += 1
        ganhour += 1
    ganday += 1

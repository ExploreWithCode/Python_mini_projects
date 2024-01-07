import time
from IPython.display import clear_output
print("The solar time model is used for this stopwatch. \n More info here: https://lco.global/spacebook/sky/sidereal-time/"
      " | https://science.nasa.gov/jupiter/moons/carme | \n https://en.wikipedia.org/wiki/Solar_time | https://en.wikipedia.org/wiki/Synodic_day")
ratio = (10.4*60*60) / (24*60*60)
print(f"A day on Carme, Jupiter's moon, lasts {round(ratio, 5)} Earth days.")
carmeday = 0
while carmeday <= 365:
    carmehour = 0
    while carmehour < 24:
        carmemins = 0
        while carmemins < 60:
            carmesec = 0
            while carmesec < 60:
                print(f"Carme stopwatch: {carmeday} : {carmehour} : {carmemins} : {carmesec}", end='\x1b[2K')
                time.sleep(ratio)
                clear_output()
                carmesec += 1
            carmemins += 1
        carmehour += 1
    carmeday += 1

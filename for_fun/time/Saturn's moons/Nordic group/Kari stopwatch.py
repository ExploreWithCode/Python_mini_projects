import time
from IPython.display import clear_output
print("The solar time model is used for this stopwatch. \n More info here: https://lco.global/spacebook/sky/sidereal-time/"
      " | https://science.nasa.gov/saturn/moons/kari / | \n https://en.wikipedia.org/wiki/Solar_time | https://en.wikipedia.org/wiki/Synodic_day")
ratio = 7.70 / 24
print(f"A day on Kari, Saturn's moon lasts {round(ratio, 6)} Earth days.")
kariday = 0
while kariday <= 365:
    karihour = 0
    while karihour < 24:
        karimins = 0
        while karimins < 60:
            karisec = 0
            while karisec < 60:
                print(f"Kari stopwatch: {kariday} : {karihour} : {karimins} : {karisec}", end='\x1b[2K')
                time.sleep(ratio)
                clear_output()
                karisec += 1
            karimins += 1
        karihour += 1
    kariday += 1

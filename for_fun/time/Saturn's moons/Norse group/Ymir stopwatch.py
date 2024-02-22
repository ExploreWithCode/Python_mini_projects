import time
from IPython.display import clear_output
print("The solar time model is used for this stopwatch. \n More info here: https://lco.global/spacebook/sky/sidereal-time/"
      " | https://science.nasa.gov/saturn/moons/ymir / | \n https://en.wikipedia.org/wiki/Solar_time | https://en.wikipedia.org/wiki/Synodic_day")
ratio = 11.92220 / 24
print(f"A day on Ymir, Saturn's moon lasts {round(ratio, 8)} Earth days.")
ymirday = 0
while ymirday <= 365:
    ymirhour = 0
    while ymirhour < 24:
        ymirmins = 0
        while ymirmins < 60:
            ymirsec = 0
            while ymirsec < 60:
                print(f"Ymir stopwatch: {ymirday} : {ymirhour} : {ymirmins} : {ymirsec}", end='\x1b[2K')
                time.sleep(ratio)
                clear_output()
                ymirsec += 1
            ymirmins += 1
        ymirhour += 1
    ymirday += 1

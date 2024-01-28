import time
from IPython.display import clear_output
print("The solar time model is used for this stopwatch. \n More info here: https://lco.global/spacebook/sky/sidereal-time/"
      " | https://science.nasa.gov/saturn/moons/bebhionn/ | \n https://en.wikipedia.org/wiki/Solar_time | https://en.wikipedia.org/wiki/Synodic_day")
ratio = 16.33 / 24
print(f"A day on Bebhionn, Saturn's moon lasts {round(ratio, 7)} Earth days.")
bebhionnday = 0
while bebhionnday <= 365:
    bebhionnhour = 0
    while bebhionnhour < 24:
        bebhionnmins = 0
        while bebhionnmins < 60:
            bebhionnsec = 0
            while bebhionnsec < 60:
                print(f"Bebhionn stopwatch: {bebhionnday} : {bebhionnhour} : {bebhionnmins} : {bebhionnsec}", end='\x1b[2K')
                time.sleep(ratio)
                clear_output()
                bebhionnsec += 1
            bebhionnmins += 1
        bebhionnhour += 1
    bebhionnday += 1

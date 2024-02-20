import time
from IPython.display import clear_output
print("The solar time model is used for this stopwatch. \n More info here: https://lco.global/spacebook/sky/sidereal-time/"
      " | https://science.nasa.gov/saturn/moons/loge / | \n https://en.wikipedia.org/wiki/Solar_time | https://en.wikipedia.org/wiki/Synodic_day")
ratio = 6.9 / 24
print(f"A day on Loge, Saturn's moon lasts {round(ratio, 4)} Earth days.")
logeday = 0
while logeday <= 365:
    logehour = 0
    while logehour < 24:
        logemins = 0
        while logemins < 60:
            logesec = 0
            while logesec < 60:
                print(f"Loge stopwatch: {logeday} : {logehour} : {logemins} : {logesec}", end='\x1b[2K')
                time.sleep(ratio)
                clear_output()
                logesec += 1
            logemins += 1
        logehour += 1
    logeday += 1

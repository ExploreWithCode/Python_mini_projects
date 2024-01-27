import time
from IPython.display import clear_output
print("The solar time model is used for this stopwatch. \n More info here: https://lco.global/spacebook/sky/sidereal-time/"
      " | https://science.nasa.gov/saturn/moons/albiorix/ | \n https://en.wikipedia.org/wiki/Solar_time | https://en.wikipedia.org/wiki/Synodic_day")
ratio = 13.33 / 24
print(f"A day on Albiorix, Saturn's moon lasts {round(ratio, 7)} Earth days.")
albiorixday = 0
while albiorixday <= 365:
    albiorixhour = 0
    while albiorixhour < 24:
        albiorixmins = 0
        while albiorixmins < 60:
            albiorixsec = 0
            while albiorixsec < 60:
                print(f"Albiorix stopwatch: {albiorixday} : {albiorixhour} : {albiorixmins} : {albiorixsec}", end='\x1b[2K')
                time.sleep(ratio)
                clear_output()
                albiorixsec += 1
            albiorixmins += 1
        albiorixhour += 1
    albiorixday += 1

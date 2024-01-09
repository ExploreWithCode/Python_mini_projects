import time
from IPython.display import clear_output
print("The solar time model is used for this stopwatch. \n More info here: https://lco.global/spacebook/sky/sidereal-time/"
      " | https://science.nasa.gov/jupiter/moons/sinope | \n https://en.wikipedia.org/wiki/Solar_time | https://en.wikipedia.org/wiki/Synodic_day")
ratio = (13.16*60*60) / (24*60*60)
print(f"A day on Sinope, Jupiter's moon, lasts {round(ratio, 5)} Earth days.")
sinopeday = 0
while sinopeday <= 365:
    sinopehour = 0
    while sinopehour < 24:
        sinopemins = 0
        while sinopemins < 60:
            sinopesec = 0
            while sinopesec < 60:
                print(f"Sinope stopwatch: {sinopeday} : {sinopehour} : {sinopemins} : {sinopesec}", end='\x1b[2K')
                time.sleep(ratio)
                clear_output()
                sinopesec += 1
            sinopemins += 1
        sinopehour += 1
    sinopeday += 1

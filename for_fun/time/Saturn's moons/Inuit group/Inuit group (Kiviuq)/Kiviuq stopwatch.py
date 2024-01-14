import time
from IPython.display import clear_output
print("The solar time model is used for this stopwatch. \n More info here: https://lco.global/spacebook/sky/sidereal-time/"
      " | https://science.nasa.gov/saturn/moons/kiviuq/ | \n https://en.wikipedia.org/wiki/Solar_time | https://en.wikipedia.org/wiki/Synodic_day")
ratio = 21.97 / 24
print(f"A day on Kiviuq, Saturn's moon lasts {round(ratio, 7)} Earth days.")
kiviuqday = 0
while kiviuqday <= 365:
    kiviuqhour = 0
    while kiviuqhour < 24:
        kiviuqmins = 0
        while kiviuqmins < 60:
            kiviuqsec = 0
            while kiviuqsec < 60:
                print(f"Kiviuq stopwatch: {kiviuqday} : {kiviuqhour} : {kiviuqmins} : {kiviuqsec}", end='\x1b[2K')
                time.sleep(ratio)
                clear_output()
                kiviuqsec += 1
            kiviuqmins += 1
        kiviuqhour += 1
    kiviuqday += 1

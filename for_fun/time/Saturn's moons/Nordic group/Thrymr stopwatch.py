import time
from IPython.display import clear_output
print("The solar time model is used for this stopwatch. \n More info here: https://lco.global/spacebook/sky/sidereal-time/"
      " | https://science.nasa.gov/saturn/moons/thrymr / | \n https://en.wikipedia.org/wiki/Solar_time | https://en.wikipedia.org/wiki/Synodic_day")
ratio = 38.79 / 24
print(f"A day on Thrymr, Saturn's moon lasts {ratio} Earth days.")
thrymrday = 0
while thrymrday <= 365:
    thrymrhour = 0
    while thrymrhour < 24:
        thrymrmins = 0
        while thrymrmins < 60:
            thrymrsec = 0
            while thrymrsec < 60:
                print(f"Thrymr stopwatch: {thrymrday} : {thrymrhour} : {thrymrmins} : {thrymrsec}", end='\x1b[2K')
                time.sleep(ratio)
                clear_output()
                thrymrsec += 1
            thrymrmins += 1
        thrymrhour += 1
    thrymrday += 1

import time
from IPython.display import clear_output
print("The solar time model is used for this stopwatch. \n More info here: https://lco.global/spacebook/sky/sidereal-time/"
      " | https://science.nasa.gov/saturn/moons/bestla / | \n https://en.wikipedia.org/wiki/Solar_time | https://en.wikipedia.org/wiki/Synodic_day")
ratio = 14.6238 / 24
print(f"A day on Bestla, Saturn's moon lasts {ratio} Earth days.")
bestladay = 0
while bestladay <= 365:
    bestlahour = 0
    while bestlahour < 24:
        bestlamins = 0
        while bestlamins < 60:
            bestlasec = 0
            while bestlasec < 60:
                print(f"Bestla stopwatch: {bestladay} : {bestlahour} : {bestlamins} : {bestlasec}", end='\x1b[2K')
                time.sleep(ratio)
                clear_output()
                bestlasec += 1
            bestlamins += 1
        bestlahour += 1
    bestladay += 1

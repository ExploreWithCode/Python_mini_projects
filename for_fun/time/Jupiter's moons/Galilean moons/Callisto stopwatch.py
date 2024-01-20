import time
from IPython.display import clear_output
print("The solar time model is used for this stopwatch. \n More info here: https://lco.global/spacebook/sky/sidereal-time/"
      " | https://science.nasa.gov/jupiter/moons/callisto/facts/ | \n https://en.wikipedia.org/wiki/Solar_time | https://en.wikipedia.org/wiki/Synodic_day")
ratio = 16.6890184
print(f"A day on Callisto, Jupiter's moon, lasts {ratio} Earth days.")
calday = 0
while calday <= 365:
    calhour = 0
    while calhour < 24:
        calmins = 0
        while calmins < 60:
            calsec = 0
            while calsec < 60:
                print(f"Callisto stopwatch: {calday} : {calhour} : {calmins} : {calsec}", end='\x1b[2K')
                time.sleep(ratio)
                clear_output()
                calsec += 1
            calmins += 1
        calhour += 1
    calday += 1

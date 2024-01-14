import time
from IPython.display import clear_output
print("The solar time model is used for this stopwatch. \n More info here: https://lco.global/spacebook/sky/sidereal-time/"
      " | https://science.nasa.gov/saturn/moons/rhea/ | \n https://en.wikipedia.org/wiki/Solar_time | https://en.wikipedia.org/wiki/Synodic_day")
ratio = 4.518212
print(f"A day on Rhea, Saturn's moon lasts {ratio} Earth days.")
rheaday = 0
while rheaday <= 365:
    rheahour = 0
    while rheahour < 24:
        rheamins = 0
        while rheamins < 60:
            rheasec = 0
            while rheasec < 60:
                print(f"Rhea stopwatch: {rheaday} : {rheahour} : {rheamins} : {rheasec}", end='\x1b[2K')
                time.sleep(ratio)
                clear_output()
                rheasec += 1
            rheamins += 1
        rheahour += 1
    rheaday += 1

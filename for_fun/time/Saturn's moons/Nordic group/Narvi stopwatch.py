import time
from IPython.display import clear_output
print("The solar time model is used for this stopwatch. \n More info here: https://lco.global/spacebook/sky/sidereal-time/"
      " | https://science.nasa.gov/saturn/moons/narvi / | \n https://en.wikipedia.org/wiki/Solar_time | https://en.wikipedia.org/wiki/Synodic_day")
ratio = 10.21 / 24
print(f"A day on Narvi, Saturn's moon lasts {round(ratio, 7)} Earth days.")
narviday = 0
while narviday <= 365:
    narvihour = 0
    while narvihour < 24:
        narvimins = 0
        while narvimins < 60:
            narvisec = 0
            while narvisec < 60:
                print(f"Narvi stopwatch: {narviday} : {narvihour} : {narvimins} : {narvisec}", end='\x1b[2K')
                time.sleep(ratio)
                clear_output()
                narvisec += 1
            narvimins += 1
        narvihour += 1
    narviday += 1

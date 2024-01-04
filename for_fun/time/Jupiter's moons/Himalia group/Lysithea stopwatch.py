import time
from IPython.display import clear_output
print("The solar time model is used for this stopwatch. \n More info here: https://lco.global/spacebook/sky/sidereal-time/"
      " | https://science.nasa.gov/jupiter/moons/lysithea | \n https://en.wikipedia.org/wiki/Solar_time | https://en.wikipedia.org/wiki/Synodic_day")
ratio = (12.78*60*60) / (24*60*60)
print(f"A day on Lysithea, Jupiter's moon, lasts {ratio} Earth days.")
lysday = 0
while lysday <= 365:
    lyshour = 0
    while lyshour < 24:
        lysmins = 0
        while lysmins < 60:
            lyssec = 0
            while lyssec < 60:
                print(f"Lysithea stopwatch: {lysday} : {lyshour} : {lysmins} : {lyssec}", end='\x1b[2K')
                time.sleep(ratio)
                clear_output()
                lyssec += 1
            lysmins += 1
        lyshour += 1
    lysday += 1

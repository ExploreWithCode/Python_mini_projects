import time
from IPython.display import clear_output
print("The solar time model is used for this stopwatch. \n More info here: https://lco.global/spacebook/sky/sidereal-time/"
      " | https://science.nasa.gov/saturn/moons/erriapus/ | \n https://en.wikipedia.org/wiki/Solar_time | https://en.wikipedia.org/wiki/Synodic_day")
ratio = 28.15 / 24
print(f"A day on Erriapus, Saturn's moon lasts {round(ratio, 7)} Earth days.")
erriapusday = 0
while erriapusday <= 365:
    erriapushour = 0
    while erriapushour < 24:
        erriapusmins = 0
        while erriapusmins < 60:
            erriapussec = 0
            while erriapussec < 60:
                print(f"Erriapus stopwatch: {erriapusday} : {erriapushour} : {erriapusmins} : {erriapussec}", end='\x1b[2K')
                time.sleep(ratio)
                clear_output()
                erriapussec += 1
            erriapusmins += 1
        erriapushour += 1
    erriapusday += 1

import time
from IPython.display import clear_output
print("The solar time model is used for this stopwatch. \n More info here: https://lco.global/spacebook/sky/sidereal-time/"
      " | https://science.nasa.gov/saturn/moons/skathi/ | \n https://en.wikipedia.org/wiki/Solar_time | https://en.wikipedia.org/wiki/Synodic_day")
ratio = 11.10 / 24
print(f"A day on Skathi, Saturn's moon lasts {round(ratio, 4)} Earth days.")
skathiday = 0
while skathiday <= 365:
    skathihour = 0
    while skathihour < 24:
        skathimins = 0
        while skathimins < 60:
            skathisec = 0
            while skathisec < 60:
                print(f"Skathi stopwatch: {skathiday} : {skathihour} : {skathimins} : {skathisec}", end='\x1b[2K')
                time.sleep(ratio)
                clear_output()
                skathisec += 1
            skathimins += 1
        skathihour += 1
    skathiday += 1

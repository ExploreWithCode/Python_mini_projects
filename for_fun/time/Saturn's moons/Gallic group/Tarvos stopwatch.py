import time
from IPython.display import clear_output
print("The solar time model is used for this stopwatch. \n More info here: https://lco.global/spacebook/sky/sidereal-time/"
      " | https://science.nasa.gov/saturn/moons/tarvos/ | \n https://en.wikipedia.org/wiki/Solar_time | https://en.wikipedia.org/wiki/Synodic_day")
ratio = 10.691 / 24
print(f"A day on Tarvos, Saturn's moon lasts {round(ratio, 8)} Earth days.")
tarvosday = 0
while tarvosday <= 365:
    tarvoshour = 0
    while tarvoshour < 24:
        tarvosmins = 0
        while tarvosmins < 60:
            tarvossec = 0
            while tarvossec < 60:
                print(f"Tarvos stopwatch: {tarvosday} : {tarvoshour} : {tarvosmins} : {tarvossec}", end='\x1b[2K')
                time.sleep(ratio)
                clear_output()
                tarvossec += 1
            tarvosmins += 1
        tarvoshour += 1
    tarvosday += 1

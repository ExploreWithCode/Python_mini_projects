import time
from IPython.display import clear_output
print("The solar time model is used for this stopwatch. \n More info here: https://lco.global/spacebook/sky/sidereal-time/"
      " | https://science.nasa.gov/saturn/moons/iapetus/ | \n https://en.wikipedia.org/wiki/Solar_time | https://en.wikipedia.org/wiki/Synodic_day")
ratio = 79.3215
print(f"A day on Iapetus, Saturn's moon lasts {ratio} Earth days.")
iapetusday = 0
while iapetusday <= 365:
    iapetushour = 0
    while iapetushour < 24:
        iapetusmins = 0
        while iapetusmins < 60:
            iapetussec = 0
            while iapetussec < 60:
                print(f"Iapetus stopwatch: {iapetusday} : {iapetushour} : {iapetusmins} : {iapetussec}", end='\x1b[2K')
                time.sleep(ratio)
                clear_output()
                iapetussec += 1
            iapetusmins += 1
        iapetushour += 1
    iapetusday += 1

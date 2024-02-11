import time
from IPython.display import clear_output
print("The solar time model is used for this stopwatch. \n More info here: https://lco.global/spacebook/sky/sidereal-time/"
      " | https://science.nasa.gov/saturn/moons/hyrrokkin / | \n https://en.wikipedia.org/wiki/Solar_time | https://en.wikipedia.org/wiki/Synodic_day")
ratio = 12.76 / 24
print(f"A day on Hyrrokkin, Saturn's moon lasts {round(ratio, 5)} Earth days.")
hyrrokkinday = 0
while hyrrokkinday <= 365:
    hyrrokkinhour = 0
    while hyrrokkinhour < 24:
        hyrrokkinmins = 0
        while hyrrokkinmins < 60:
            hyrrokkinsec = 0
            while hyrrokkinsec < 60:
                print(f"Hyrrokkin stopwatch: {hyrrokkinday} : {hyrrokkinhour} : {hyrrokkinmins} : {hyrrokkinsec}", end='\x1b[2K')
                time.sleep(ratio)
                clear_output()
                hyrrokkinsec += 1
            hyrrokkinmins += 1
        hyrrokkinhour += 1
    hyrrokkinday += 1

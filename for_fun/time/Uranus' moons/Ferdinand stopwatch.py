import time
from IPython.display import clear_output
print("The solar time model is used for this stopwatch. \n More info here: https://lco.global/spacebook/sky/sidereal-time/"
      " | https://science.nasa.gov/uranus/moons/ferdinand/ | \n https://en.wikipedia.org/wiki/Solar_time | https://en.wikipedia.org/wiki/Synodic_day")
ratio = 11.84 / 24
print(f"A day on Ferdinand, Uranus' moon lasts {round(ratio, 4)} Earth days.")
ferdinandday = 0
while ferdinandday <= 365:
    ferdinandhour = 0
    while ferdinandhour < 24:
        ferdinandmins = 0
        while ferdinandmins < 60:
            ferdinandsec = 0
            while ferdinandsec < 60:
                print(f"Ferdinand stopwatch: {ferdinandday} : {ferdinandhour} : {ferdinandmins} : {ferdinandsec}", end='\x1b[2K')
                time.sleep(ratio)
                clear_output()
                ferdinandsec += 1
            ferdinandmins += 1
        ferdinandhour += 1
    ferdinandday += 1

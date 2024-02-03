import time
from IPython.display import clear_output
print("The solar time model is used for this stopwatch. \n More info here: https://lco.global/spacebook/sky/sidereal-time/"
      " | https://science.nasa.gov/saturn/moons/hyperion/ | \n https://en.wikipedia.org/wiki/Solar_time | https://en.wikipedia.org/wiki/Synodic_day")
ratio = 13
print(f"A day on Hyperion, Saturn's moon lasts {ratio} Earth days.")
hyperionday = 0
while hyperionday <= 365:
    hyperionhour = 0
    while hyperionhour < 24:
        hyperionmins = 0
        while hyperionmins < 60:
            hyperionsec = 0
            while hyperionsec < 60:
                print(f"Hyperion stopwatch: {hyperionday} : {hyperionhour} : {hyperionmins} : {hyperionsec}", end='\x1b[2K')
                time.sleep(ratio)
                clear_output()
                hyperionsec += 1
            hyperionmins += 1
        hyperionhour += 1
    hyperionday += 1

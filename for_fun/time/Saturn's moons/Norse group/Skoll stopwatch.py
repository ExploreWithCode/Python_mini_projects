import time
from IPython.display import clear_output
print("The solar time model is used for this stopwatch. \n More info here: https://lco.global/spacebook/sky/sidereal-time/"
      " | https://science.nasa.gov/saturn/moons/skoll / | \n https://en.wikipedia.org/wiki/Solar_time | https://en.wikipedia.org/wiki/Synodic_day")
ratio = 7.26 / 24
print(f"A day on Skoll, Saturn's moon lasts {ratio} Earth days.")
skollday = 0
while skollday <= 365:
    skollhour = 0
    while skollhour < 24:
        skollmins = 0
        while skollmins < 60:
            skollsec = 0
            while skollsec < 60:
                print(f"Skoll stopwatch: {skollday} : {skollhour} : {skollmins} : {skollsec}", end='\x1b[2K')
                time.sleep(ratio)
                clear_output()
                skollsec += 1
            skollmins += 1
        skollhour += 1
    skollday += 1

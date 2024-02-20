import time
from IPython.display import clear_output
print("The solar time model is used for this stopwatch. \n More info here: https://lco.global/spacebook/sky/sidereal-time/"
      " | https://science.nasa.gov/saturn/moons/suttungr / | \n https://en.wikipedia.org/wiki/Solar_time | https://en.wikipedia.org/wiki/Synodic_day")
ratio = 7.67 / 24
print(f"A day on Suttungr, Saturn's moon lasts {round(ratio, 7)} Earth days.")
suttungrday = 0
while suttungrday <= 365:
    suttungrhour = 0
    while suttungrhour < 24:
        suttungrmins = 0
        while suttungrmins < 60:
            suttungrsec = 0
            while suttungrsec < 60:
                print(f"Suttungr stopwatch: {suttungrday} : {suttungrhour} : {suttungrmins} : {suttungrsec}", end='\x1b[2K')
                time.sleep(ratio)
                clear_output()
                suttungrsec += 1
            suttungrmins += 1
        suttungrhour += 1
    suttungrday += 1

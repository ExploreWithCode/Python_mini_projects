import time
from IPython.display import clear_output
print("The solar time model is used for this stopwatch. \n More info here: https://lco.global/spacebook/sky/sidereal-time/"
      " | https://science.nasa.gov/saturn/moons/greip / | \n https://en.wikipedia.org/wiki/Solar_time | https://en.wikipedia.org/wiki/Synodic_day")
ratio = 12.75 / 24
print(f"A day on Greip, Saturn's moon lasts {ratio} Earth days.")
greipday = 0
while greipday <= 365:
    greiphour = 0
    while greiphour < 24:
        greipmins = 0
        while greipmins < 60:
            greipsec = 0
            while greipsec < 60:
                print(f"Greip stopwatch: {greipday} : {greiphour} : {greipmins} : {greipsec}", end='\x1b[2K')
                time.sleep(ratio)
                clear_output()
                greipsec += 1
            greipmins += 1
        greiphour += 1
    greipday += 1

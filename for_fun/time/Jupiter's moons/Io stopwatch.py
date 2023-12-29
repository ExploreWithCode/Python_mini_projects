import time
from IPython.display import clear_output
print("The solar time model is used for this stopwatch. \n More info here: https://lco.global/spacebook/sky/sidereal-time/"
      " | https://science.nasa.gov/jupiter/moons/io/facts/ | \n https://en.wikipedia.org/wiki/Solar_time | https://en.wikipedia.org/wiki/Synodic_day")
ratio = 1.7624
print(f"A day on Io, Jupiter's moon, lasts {ratio} Earth days.")
ioday = 0
while ioday <= 365:
    iohour = 0
    while iohour < 24:
        iomins = 0
        while iomins < 60:
            iosec = 0
            while iosec < 60:
                print(f"Io stopwatch: {ioday} : {iohour} : {iomins} : {iosec}", end='\x1b[2K')
                time.sleep(ratio)
                clear_output()
                iosec += 1
            iomins += 1
        iohour += 1
    ioday += 1

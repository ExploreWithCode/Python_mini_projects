import time
from IPython.display import clear_output
print("The solar time model is used for this stopwatch. \n More info here: https://lco.global/spacebook/sky/sidereal-time/"
      " | https://science.nasa.gov/saturn/moons/mundilfari / | \n https://en.wikipedia.org/wiki/Solar_time | https://en.wikipedia.org/wiki/Synodic_day")
ratio = 6.74 / 24
print(f"A day on Mundilfari, Saturn's moon lasts {round(ratio, 6)} Earth days.")
mundilfariday = 0
while mundilfariday <= 365:
    mundilfarihour = 0
    while mundilfarihour < 24:
        mundilfarimins = 0
        while mundilfarimins < 60:
            mundilfarisec = 0
            while mundilfarisec < 60:
                print(f"Mundilfari stopwatch: {mundilfariday} : {mundilfarihour} : {mundilfarimins} : {mundilfarisec}", end='\x1b[2K')
                time.sleep(ratio)
                clear_output()
                mundilfarisec += 1
            mundilfarimins += 1
        mundilfarihour += 1
    mundilfariday += 1

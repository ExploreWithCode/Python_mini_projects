import time
from IPython.display import clear_output
print("The solar time model is used for this stopwatch. \n More info here: https://lco.global/spacebook/sky/sidereal-time/"
      " | https://science.nasa.gov/saturn/moons/bergelmir / | \n https://en.wikipedia.org/wiki/Solar_time | https://en.wikipedia.org/wiki/Synodic_day")
ratio = 8.13 / 24
print(f"A day on Bergelmir, Saturn's moon lasts {round(ratio, 5)} Earth days.")
bergelmirday = 0
while bergelmirday <= 365:
    bergelmirhour = 0
    while bergelmirhour < 24:
        bergelmirmins = 0
        while bergelmirmins < 60:
            bergelmirsec = 0
            while bergelmirsec < 60:
                print(f"Bergelmir stopwatch: {bergelmirday} : {bergelmirhour} : {bergelmirmins} : {bergelmirsec}", end='\x1b[2K')
                time.sleep(ratio)
                clear_output()
                bergelmirsec += 1
            bergelmirmins += 1
        bergelmirhour += 1
    bergelmirday += 1

import time
from IPython.display import clear_output
print("The solar time model is used for this stopwatch. \n More info here: https://lco.global/spacebook/sky/sidereal-time/"
      " | https://science.nasa.gov/dwarf-planets/pluto/facts/ | \n https://en.wikipedia.org/wiki/Solar_time | https://en.wikipedia.org/wiki/Synodic_day")
ratio = ((6*24*60*60)+(9*60*60)+(17*60)) / (24*60*60)
print(f'A day on Pluto, a dwarf planet, lasts {round(ratio, 4)} Earth days.')
plutoday = 0
while plutoday <= 365:
    plutohour = 0
    while plutohour < 24:
        plutomins = 0
        while plutomins < 60:
            plutosec = 0
            while plutosec < 60:
                print(f"Pluto stopwatch: {plutoday} : {plutohour} : {plutomins} : {plutosec}", end='\x1b[2K')
                time.sleep(ratio)
                clear_output()
                plutosec += 1
            plutomins += 1
        plutohour += 1
    plutoday += 1

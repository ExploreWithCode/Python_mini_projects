import time
from IPython.display import clear_output
print("The solar time model is used for this stopwatch. \n More info here: https://lco.global/spacebook/sky/sidereal-time/"
      " | https://en.wikipedia.org/wiki/90377_Sedna | \n https://en.wikipedia.org/wiki/Solar_time | https://en.wikipedia.org/wiki/Synodic_day")
ratio = 10.273 / 24
print(f'A day on Sedna, a dwarf planet lasts {round(ratio, 7)} Earth days.')
sednaday = 0
while sednaday <= 365:
    sednahour = 0
    while sednahour < 24:
        sednamins = 0
        while sednamins < 60:
            sednasec = 0
            while sednasec < 60:
                print(f"Sedna stopwatch: {sednaday} : {sednahour} : {sednamins} : {sednasec}", end='\x1b[2K')
                time.sleep(ratio)
                clear_output()
                sednasec += 1
            sednamins += 1
        sednahour += 1
    sednaday += 1

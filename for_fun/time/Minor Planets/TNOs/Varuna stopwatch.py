import time
from IPython.display import clear_output
print("The solar time model is used for this stopwatch. \n More info here: https://lco.global/spacebook/sky/sidereal-time/"
      " | https://en.wikipedia.org/wiki/20000_Varuna | \n https://en.wikipedia.org/wiki/Solar_time | https://en.wikipedia.org/wiki/Synodic_day")
ratio = 6.343572 / 24
print(f'A day on Varuna, a cubewano, lasts {ratio} Earth days.')
varunaday = 0
while varunaday <= 365:
    varunahour = 0
    while varunahour < 24:
        varunamins = 0
        while varunamins < 60:
            varunasec = 0
            while varunasec < 60:
                print(f"Varuna stopwatch: {varunaday} : {varunahour} : {varunamins} : {varunasec}", end='\x1b[2K')
                time.sleep(ratio)
                clear_output()
                varunasec += 1
            varunamins += 1
        varunahour += 1
    varunaday += 1

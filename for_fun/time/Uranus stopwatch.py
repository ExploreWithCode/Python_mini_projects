import time
from IPython.display import clear_output
print("The solar time model is used for this stopwatch. \n More info here: https://lco.global/spacebook/sky/sidereal-time/"
      " | https://science.nasa.gov/uranus/facts/ | \n https://en.wikipedia.org/wiki/Solar_time | https://en.wikipedia.org/wiki/Synodic_day")
ratio = ((17*60*60)+(14*60)+23) / (24*60*60)
print(f'A day on Uranus lasts {ratio} Earth days.')
uraday = 0
while uraday <= 365:
    urahour = 0
    while urahour < 24:
        uramins = 0
        while uramins < 60:
            urasec = 0
            while urasec < 60:
                print(f"Uranus stopwatch: {uraday} : {urahour} : {uramins} : {urasec}", end='\x1b[2K')
                time.sleep(ratio)
                clear_output()
                urasec += 1
            uramins += 1
        urahour += 1
    uraday += 1

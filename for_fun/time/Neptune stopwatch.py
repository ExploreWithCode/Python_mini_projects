import time
from IPython.display import clear_output
print("The solar time model is used for this stopwatch. \n More info here: https://lco.global/spacebook/sky/sidereal-time/"
      " | https://science.nasa.gov/neptune/facts/ | \n https://en.wikipedia.org/wiki/Solar_time | https://en.wikipedia.org/wiki/Synodic_day")
ratio = ((16*60*60)+(6*60)+36) / (24*60*60)
print(f'A day on Neptune lasts {ratio} Earth days.')
nepday = 0
while nepday <= 365:
    nephour = 0
    while nephour < 24:
        nepmins = 0
        while nepmins < 60:
            nepsec = 0
            while nepsec < 60:
                print(f"Neptune stopwatch: {nepday} : {nephour} : {nepmins} : {nepsec}", end='\x1b[2K')
                time.sleep(ratio)
                clear_output()
                nepsec += 1
            nepmins += 1
        nephour += 1
    nepday += 1

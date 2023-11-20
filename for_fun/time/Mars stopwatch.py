import time
from IPython.display import clear_output
print("The solar time model is used for this stopwatch. \n More info here: https://lco.global/spacebook/sky/sidereal-time/"
      " | https://en.wikipedia.org/wiki/Mars_sol | \n https://en.wikipedia.org/wiki/Solar_time | https://en.wikipedia.org/wiki/Synodic_day")
ratio = ((24*60*60)+(39*60)+35.244) / (24*60*60)
print(f'A day on Mars lasts {ratio} Earth days.')
mday = 0
while mday <= 365:
    mhour = 0
    while mhour < 24:
        mmins = 0
        while mmins < 60:
            msec = 0
            while msec < 60:
                print(f"Mars stopwatch: {mday} : {mhour} : {mmins} : {msec}", end='\x1b[2K')
                time.sleep(ratio)
                clear_output()
                msec += 1
            mmins += 1
        mhour += 1
    mday += 1

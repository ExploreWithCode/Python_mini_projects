import time
from IPython.display import clear_output
print("The solar time model is used for this stopwatch. \n More info here: https://lco.global/spacebook/sky/sidereal-time/"
      " | https://science.nasa.gov/venus/facts/ | \n https://en.wikipedia.org/wiki/Solar_time | https://en.wikipedia.org/wiki/Synodic_day")
ratio = 116.75
print(f'A day on Venus lasts {ratio} Earth days.')
vday = 0
while vday <= 365:
    vhour = 0
    while vhour < 24:
        vmins = 0
        while vmins < 60:
            vsec = 0
            while vsec < 60:
                print(f"Venus stopwatch: {vday} : {vhour} : {vmins} : {vsec}", end='\x1b[2K')
                time.sleep(ratio)
                clear_output()
                vsec += 1
            vmins += 1
        vhour += 1
    vday += 1

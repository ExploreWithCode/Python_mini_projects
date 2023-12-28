import time
from IPython.display import clear_output
print("The solar time model is used for this stopwatch. \n More info here: https://lco.global/spacebook/sky/sidereal-time/"
      " | https://science.nasa.gov/mercury/facts/ | \n https://en.wikipedia.org/wiki/Solar_time | https://en.wikipedia.org/wiki/Synodic_day")
ratio = 176.2155
print(f'A day on Mercury lasts {ratio} Earth days.')
merday = 0
while merday <= 365:
    merhour = 0
    while merhour < 24:
        mermins = 0
        while mermins < 60:
            mersec = 0
            while mersec < 60:
                print(f"Mercury stopwatch: {merday} : {merhour} : {mermins} : {mersec}", end='\x1b[2K')
                time.sleep(ratio)
                clear_output()
                mersec += 1
            mermins += 1
        merhour += 1
    merday += 1

import time
from IPython.display import clear_output
print("The solar time model is used for this stopwatch. \n More info here: https://lco.global/spacebook/sky/sidereal-time/"
      " | https://en.wikipedia.org/wiki/Hydra_(moon) | \n https://en.wikipedia.org/wiki/Solar_time | https://en.wikipedia.org/wiki/Synodic_day")
ratio = 10.31 / 24
print(f'A day on Hydra, a moon of the dwarf planet Pluto, lasts {round(ratio, 7)} Earth days.')
hydraday = 0
while hydraday <= 365:
    hydrahour = 0
    while hydrahour < 24:
        hydramins = 0
        while hydramins < 60:
            hydrasec = 0
            while hydrasec < 60:
                print(f"Hydra stopwatch: {hydraday} : {hydrahour} : {hydramins} : {hydrasec}", end='\x1b[2K')
                time.sleep(ratio)
                clear_output()
                hydrasec += 1
            hydramins += 1
        hydrahour += 1
    hydraday += 1

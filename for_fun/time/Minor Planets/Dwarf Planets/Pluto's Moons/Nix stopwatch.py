import time
from IPython.display import clear_output
print("The solar time model is used for this stopwatch. \n More info here: https://lco.global/spacebook/sky/sidereal-time/"
      " | https://en.wikipedia.org/wiki/Nix_(moon) | \n https://en.wikipedia.org/wiki/Solar_time | https://en.wikipedia.org/wiki/Synodic_day")
ratio = 1.829
print(f'A day on Nix, a moon of the dwarf planet Pluto, lasts {ratio} Earth days.')
nixday = 0
while nixday <= 365:
    nixhour = 0
    while nixhour < 24:
        nixmins = 0
        while nixmins < 60:
            nixsec = 0
            while nixsec < 60:
                print(f"Nix stopwatch: {nixday} : {nixhour} : {nixmins} : {nixsec}", end='\x1b[2K')
                time.sleep(ratio)
                clear_output()
                nixsec += 1
            nixmins += 1
        nixhour += 1
    nixday += 1

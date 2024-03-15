import time
from IPython.display import clear_output
print("The solar time model is used for this stopwatch. \n More info here: https://lco.global/spacebook/sky/sidereal-time/"
      " | https://science.nasa.gov/uranus/moons/caliban/ | \n https://en.wikipedia.org/wiki/Solar_time | https://en.wikipedia.org/wiki/Synodic_day")
ratio1 = 2.66 / 24
ratio2 = 9.948 / 24
print(f"A day on Caliban, Uranus' moon lasts this many Earth days:\n"
      f"single-peaked: {round(ratio1, 6)}\n"
      f"double-peaked: {round(ratio2, 4)}\n")
inp = input("Pick a scenario:'1' for single-peaked or '2' for double-peaked\n")
if inp == "1":
    calibanday = 0
    while calibanday <= 365:
        calibanhour = 0
        while calibanhour < 24:
            calibanmins = 0
            while calibanmins < 60:
                calibansec = 0
                while calibansec < 60:
                    print(f"Caliban stopwatch: {calibanday} : {calibanhour} : {calibanmins} : {calibansec}", end='\x1b[2K')
                    time.sleep(ratio1)
                    clear_output()
                    calibansec += 1
                calibanmins += 1
            calibanhour += 1
        calibanday += 1
elif inp == "2":
    calibanday = 0
    while calibanday <= 365:
        calibanhour = 0
        while calibanhour < 24:
            calibanmins = 0
            while calibanmins < 60:
                calibansec = 0
                while calibansec < 60:
                    print(f"Caliban stopwatch: {calibanday} : {calibanhour} : {calibanmins} : {calibansec}", end='\x1b[2K')
                    time.sleep(ratio2)
                    clear_output()
                    calibansec += 1
                calibanmins += 1
            calibanhour += 1
        calibanday += 1
else:
    print("Wrong number!")

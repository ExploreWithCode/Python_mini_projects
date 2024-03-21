import time
from IPython.display import clear_output
print("The solar time model is used for this stopwatch. \n More info here: https://lco.global/spacebook/sky/sidereal-time/"
      " | https://science.nasa.gov/uranus/moons/sycorax/ | \n https://en.wikipedia.org/wiki/Solar_time | https://en.wikipedia.org/wiki/Synodic_day")
ratio1 = 3.6 / 24
ratio2 = 6.9162 / 24
print(f"A day on Sycorax, Uranus' moon lasts this many Earth days:\n"
      f"single-peaked: {ratio1}\n"
      f"double-peaked: {ratio2}\n")
inp = input("Pick a scenario:'1' for single-peaked or '2' for double-peaked\n")
if inp == "1":
    sycoraxday = 0
    while sycoraxday <= 365:
        sycoraxhour = 0
        while sycoraxhour < 24:
            sycoraxmins = 0
            while sycoraxmins < 60:
                sycoraxsec = 0
                while sycoraxsec < 60:
                    print(f"Sycorax stopwatch: {sycoraxday} : {sycoraxhour} : {sycoraxmins} : {sycoraxsec}", end='\x1b[2K')
                    time.sleep(ratio1)
                    clear_output()
                    sycoraxsec += 1
                sycoraxmins += 1
            sycoraxhour += 1
        sycoraxday += 1
elif inp == "2":
    sycoraxday = 0
    while sycoraxday <= 365:
        sycoraxhour = 0
        while sycoraxhour < 24:
            sycoraxmins = 0
            while sycoraxmins < 60:
                sycoraxsec = 0
                while sycoraxsec < 60:
                    print(f"Sycorax stopwatch: {sycoraxday} : {sycoraxhour} : {sycoraxmins} : {sycoraxsec}", end='\x1b[2K')
                    time.sleep(ratio2)
                    clear_output()
                    sycoraxsec += 1
                sycoraxmins += 1
            sycoraxhour += 1
        sycoraxday += 1
else:
    print("Wrong number!")

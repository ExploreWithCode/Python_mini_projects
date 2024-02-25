import time
from IPython.display import clear_output
print("The solar time model is used for this stopwatch. \n More info here: https://lco.global/spacebook/sky/sidereal-time/"
      " | https://en.wikipedia.org/wiki/225088_Gonggong | \n https://en.wikipedia.org/wiki/Solar_time | https://en.wikipedia.org/wiki/Synodic_day")
ratio1 = 22.40 / 24
ratio2 = 44.81 / 24
print(f'A day on Gonggong, a dwarf planet lasts {round(ratio1, 3)} Earth days.\n'
      f'A less likely scenario is {round(ratio2, 7)} days.')
inp = input("Pick a scenario: 1 or 2\n")
if inp == "1":
    gonggongday = 0
    while gonggongday <= 365:
        gonggonghour = 0
        while gonggonghour < 24:
            gonggongmins = 0
            while gonggongmins < 60:
                gonggongsec = 0
                while gonggongsec < 60:
                    print(f"Gonggong stopwatch: {gonggongday} : {gonggonghour} : {gonggongmins} : {gonggongsec}",
                          end='\x1b[2K')
                    time.sleep(ratio1)
                    clear_output()
                    gonggongsec += 1
                gonggongmins += 1
            gonggonghour += 1
        gonggongday += 1
if inp == "2":
    gonggongday = 0
    while gonggongday <= 365:
        gonggonghour = 0
        while gonggonghour < 24:
            gonggongmins = 0
            while gonggongmins < 60:
                gonggongsec = 0
                while gonggongsec < 60:
                    print(f"Gonggong stopwatch: {gonggongday} : {gonggonghour} : {gonggongmins} : {gonggongsec}",
                          end='\x1b[2K')
                    time.sleep(ratio2)
                    clear_output()
                    gonggongsec += 1
                gonggongmins += 1
            gonggonghour += 1
        gonggongday += 1
else:
    print("Wrong number!")

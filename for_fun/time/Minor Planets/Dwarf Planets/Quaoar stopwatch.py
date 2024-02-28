import time
from IPython.display import clear_output
print("The solar time model is used for this stopwatch. \n More info here: https://lco.global/spacebook/sky/sidereal-time/"
      " | https://en.wikipedia.org/wiki/50000_Quaoar | \n https://en.wikipedia.org/wiki/Solar_time | https://en.wikipedia.org/wiki/Synodic_day")
ratio = 17.6788 / 24
print(f'A day on Quaoar, a dwarf planet lasts {round(ratio, 7)} Earth days.')
quaoarday = 0
while quaoarday <= 365:
    quaoarhour = 0
    while quaoarhour < 24:
        quaoarmins = 0
        while quaoarmins < 60:
            quaoarsec = 0
            while quaoarsec < 60:
                print(f"Quaoar stopwatch: {quaoarday} : {quaoarhour} : {quaoarmins} : {quaoarsec}", end='\x1b[2K')
                time.sleep(ratio)
                clear_output()
                quaoarsec += 1
            quaoarmins += 1
        quaoarhour += 1
    quaoarday += 1

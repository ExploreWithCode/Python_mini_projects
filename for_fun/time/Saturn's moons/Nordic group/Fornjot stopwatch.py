import time
from IPython.display import clear_output
print("The solar time model is used for this stopwatch. \n More info here: https://lco.global/spacebook/sky/sidereal-time/"
      " | https://science.nasa.gov/saturn/moons/fornjot / | \n https://en.wikipedia.org/wiki/Solar_time | https://en.wikipedia.org/wiki/Synodic_day")
ratio1 = 6.9 / 24
ratio2 = 9.5 / 24
print(f"A day on Fornjot, Saturn's moon lasts {round(ratio1, 4)} or {round(ratio2, 6)} Earth days.\n")


def case1():
    fornjotday = 0
    while fornjotday <= 365:
        fornjothour = 0
        while fornjothour < 24:
            fornjotmins = 0
            while fornjotmins < 60:
                fornjotsec = 0
                while fornjotsec < 60:
                    print(f"Fornjot stopwatch: {fornjotday} : {fornjothour} : {fornjotmins} : {fornjotsec}", end='\x1b[2K')
                    time.sleep(ratio1)
                    clear_output()
                    fornjotsec += 1
                fornjotmins += 1
            fornjothour += 1
        fornjotday += 1


def case2():
    fornjotday = 0
    while fornjotday <= 365:
        fornjothour = 0
        while fornjothour < 24:
            fornjotmins = 0
            while fornjotmins < 60:
                fornjotsec = 0
                while fornjotsec < 60:
                    print(f"Fornjot stopwatch: {fornjotday} : {fornjothour} : {fornjotmins} : {fornjotsec}", end='\x1b[2K')
                    time.sleep(ratio2)
                    clear_output()
                    fornjotsec += 1
                fornjotmins += 1
            fornjothour += 1
        fornjotday += 1


inpcase = input("Pick a case for the stopwatch: 1 or 2 \n")
if inpcase == "1":
    case1()
elif inpcase == "2":
    case2()
else:
    print("Wrong number!")

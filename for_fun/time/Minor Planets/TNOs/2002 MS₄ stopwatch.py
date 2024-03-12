import time
from IPython.display import clear_output
print("The solar time model is used for this stopwatch. \n More info here: https://lco.global/spacebook/sky/sidereal-time/"
      " | https://en.wikipedia.org/wiki/(307261)_2002_MS4 | \n https://en.wikipedia.org/wiki/Solar_time | https://en.wikipedia.org/wiki/Synodic_day")
ratio1 = 14.251 / 24
ratio2 = 7.33 / 24
ratio3 = 10.44 / 24

SUB = str.maketrans("0123456789", "₀₁₂₃₄₅₆₇₈₉")

print(f"A day on 2002 {"MS4".translate(SUB)}, a cubewano, lasts this many Earth days:\n"
      f"scenario 1: {round(ratio1, 8)}\n"
      f"single-peaked scenario 1: {round(ratio2, 7)}\n"
      f"single-peaked scenario 2: {ratio3}\n")
inp = input("Pick a scenario: 1, 2 or 3\n")
if inp == "1":
    _2002_MS4day = 0
    while _2002_MS4day <= 365:
        _2002_MS4hour = 0
        while _2002_MS4hour < 24:
            _2002_MS4mins = 0
            while _2002_MS4mins < 60:
                _2002_MS4sec = 0
                while _2002_MS4sec < 60:
                    print(f"2002 {"MS4".translate(SUB)} stopwatch: {_2002_MS4day} : {_2002_MS4hour} : {_2002_MS4mins} : {_2002_MS4sec}", end='\x1b[2K')
                    time.sleep(ratio1)
                    clear_output()
                    _2002_MS4sec += 1
                _2002_MS4mins += 1
            _2002_MS4hour += 1
        _2002_MS4day += 1
elif inp == "2":
    _2002_MS4day = 0
    while _2002_MS4day <= 365:
        _2002_MS4hour = 0
        while _2002_MS4hour < 24:
            _2002_MS4mins = 0
            while _2002_MS4mins < 60:
                _2002_MS4sec = 0
                while _2002_MS4sec < 60:
                    print(f"2002 {"MS4".translate(SUB)} stopwatch: {_2002_MS4day} : {_2002_MS4hour} : {_2002_MS4mins} : {_2002_MS4sec}", end='\x1b[2K')
                    time.sleep(ratio2)
                    clear_output()
                    _2002_MS4sec += 1
                _2002_MS4mins += 1
            _2002_MS4hour += 1
        _2002_MS4day += 1
elif inp == "3":
    _2002_MS4day = 0
    while _2002_MS4day <= 365:
        _2002_MS4hour = 0
        while _2002_MS4hour < 24:
            _2002_MS4mins = 0
            while _2002_MS4mins < 60:
                _2002_MS4sec = 0
                while _2002_MS4sec < 60:
                    print(f"2002 {"MS4".translate(SUB)} stopwatch: {_2002_MS4day} : {_2002_MS4hour} : {_2002_MS4mins} : {_2002_MS4sec}", end='\x1b[2K')
                    time.sleep(ratio3)
                    clear_output()
                    _2002_MS4sec += 1
                _2002_MS4mins += 1
            _2002_MS4hour += 1
        _2002_MS4day += 1
else:
    print("Wrong number!")

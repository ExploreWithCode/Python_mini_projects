import time
from IPython.display import clear_output
print("The solar time model is used for this stopwatch. \n More info here: https://lco.global/spacebook/sky/sidereal-time/"
      " | https://en.wikipedia.org/wiki/(55565)_2002_AW197 | \n https://en.wikipedia.org/wiki/Solar_time | https://en.wikipedia.org/wiki/Synodic_day")
ratio1 = 8.87 / 24
ratio2 = 8.78 / 24
ratio3 = 8.86 / 24

SUB = str.maketrans("0123456789", "₀₁₂₃₄₅₆₇₈₉")

print(f"A day on 2002 {"AW197".translate(SUB)}, a cubewano, lasts this many Earth days:\n"
      f"scenario 1: {round(ratio1, 6)}\n"
      f"scenario 2: {round(ratio2, 6)}\n"
      f"scenario 3: {round(ratio3, 6)}\n")
inp = input("Pick a scenario: 1, 2 or 3\n")
if inp == "1":
    _2002_AW197day = 0
    while _2002_AW197day <= 365:
        _2002_AW197hour = 0
        while _2002_AW197hour < 24:
            _2002_AW197mins = 0
            while _2002_AW197mins < 60:
                _2002_AW197sec = 0
                while _2002_AW197sec < 60:
                    print(f"2002 {"AW197".translate(SUB)} stopwatch: {_2002_AW197day} : {_2002_AW197hour} : {_2002_AW197mins} : {_2002_AW197sec}", end='\x1b[2K')
                    time.sleep(ratio1)
                    clear_output()
                    _2002_AW197sec += 1
                _2002_AW197mins += 1
            _2002_AW197hour += 1
        _2002_AW197day += 1
elif inp == "2":
    _2002_AW197day = 0
    while _2002_AW197day <= 365:
        _2002_AW197hour = 0
        while _2002_AW197hour < 24:
            _2002_AW197mins = 0
            while _2002_AW197mins < 60:
                _2002_AW197sec = 0
                while _2002_AW197sec < 60:
                    print(f"2002 {"AW197".translate(SUB)} stopwatch: {_2002_AW197day} : {_2002_AW197hour} : {_2002_AW197mins} : {_2002_AW197sec}", end='\x1b[2K')
                    time.sleep(ratio2)
                    clear_output()
                    _2002_AW197sec += 1
                _2002_AW197mins += 1
            _2002_AW197hour += 1
        _2002_AW197day += 1
elif inp == "3":
    _2002_AW197day = 0
    while _2002_AW197day <= 365:
        _2002_AW197hour = 0
        while _2002_AW197hour < 24:
            _2002_AW197mins = 0
            while _2002_AW197mins < 60:
                _2002_AW197sec = 0
                while _2002_AW197sec < 60:
                    print(f"2002 {"AW197".translate(SUB)} stopwatch: {_2002_AW197day} : {_2002_AW197hour} : {_2002_AW197mins} : {_2002_AW197sec}", end='\x1b[2K')
                    time.sleep(ratio3)
                    clear_output()
                    _2002_AW197sec += 1
                _2002_AW197mins += 1
            _2002_AW197hour += 1
        _2002_AW197day += 1
else:
    print("Wrong number!")

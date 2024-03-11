import time
from IPython.display import clear_output
print("The solar time model is used for this stopwatch. \n More info here: https://lco.global/spacebook/sky/sidereal-time/"
      " | https://en.wikipedia.org/wiki/(90568)_2004_GV9 | \n https://en.wikipedia.org/wiki/Solar_time | https://en.wikipedia.org/wiki/Synodic_day")
ratio = 5.86 / 24

SUB = str.maketrans("0123456789", "₀₁₂₃₄₅₆₇₈₉")
print(f'A day on 2004 {"GV9".translate(SUB)}, a cubewano, lasts {round(ratio, 6)} Earth days.')
_2004_gv9day = 0
while _2004_gv9day <= 365:
    _2004_gv9hour = 0
    while _2004_gv9hour < 24:
        _2004_gv9mins = 0
        while _2004_gv9mins < 60:
            _2004_gv9sec = 0
            while _2004_gv9sec < 60:
                print(f"2004 {"GV9".translate(SUB)} stopwatch: {_2004_gv9day} : {_2004_gv9hour} : {_2004_gv9mins} : {_2004_gv9sec}", end='\x1b[2K')
                time.sleep(ratio)
                clear_output()
                _2004_gv9sec += 1
            _2004_gv9mins += 1
        _2004_gv9hour += 1
    _2004_gv9day += 1

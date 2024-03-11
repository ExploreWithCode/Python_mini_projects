import time
from IPython.display import clear_output
print("The solar time model is used for this stopwatch. \n More info here: https://lco.global/spacebook/sky/sidereal-time/"
      " | https://en.wikipedia.org/wiki/229762_Gǃkúnǁʼhòmdímà | \n https://en.wikipedia.org/wiki/Solar_time | https://en.wikipedia.org/wiki/Synodic_day")
ratio = 11.05 / 24

SUB = str.maketrans("0123456789", "₀₁₂₃₄₅₆₇₈₉")
print(f'A day on 2007 {"UK126".translate(SUB)}, a cubewano, lasts {round(ratio, 6)} Earth days.')
_2007_UK126day = 0
while _2007_UK126day <= 365:
    _2007_UK126hour = 0
    while _2007_UK126hour < 24:
        _2007_UK126mins = 0
        while _2007_UK126mins < 60:
            _2007_UK126sec = 0
            while _2007_UK126sec < 60:
                print(f"2007 {"UK126".translate(SUB)} stopwatch: {_2007_UK126day} : {_2007_UK126hour} : {_2007_UK126mins} : {_2007_UK126sec}", end='\x1b[2K')
                time.sleep(ratio)
                clear_output()
                _2007_UK126sec += 1
            _2007_UK126mins += 1
        _2007_UK126hour += 1
    _2007_UK126day += 1

import time
from IPython.display import clear_output
print("The solar time model is used for this stopwatch. \n More info here: https://lco.global/spacebook/sky/sidereal-time/"
      " | https://en.wikipedia.org/wiki/C/2014_UN271_(Bernardinelli–Bernstein) | \n https://en.wikipedia.org/wiki/Solar_time | https://en.wikipedia.org/wiki/Synodic_day")
ratio = 20.6 / 24

SUB = str.maketrans("0123456789", "₀₁₂₃₄₅₆₇₈₉")

print(f'A day on C/2014 {"UN271".translate(SUB)}, a comet, lasts {round(ratio, 5)} Earth days.')
c_2014_un27day = 0
while c_2014_un27day <= 365:
    c_2014_un27hour = 0
    while c_2014_un27hour < 24:
        c_2014_un27mins = 0
        while c_2014_un27mins < 60:
            c_2014_un27sec = 0
            while c_2014_un27sec < 60:
                print(f"C/2014 {"UN271".translate(SUB)} stopwatch: {c_2014_un27day} : {c_2014_un27hour} : {c_2014_un27mins} : {c_2014_un27sec}", end='\x1b[2K')
                time.sleep(ratio)
                clear_output()
                c_2014_un27sec += 1
            c_2014_un27mins += 1
        c_2014_un27hour += 1
    c_2014_un27day += 1

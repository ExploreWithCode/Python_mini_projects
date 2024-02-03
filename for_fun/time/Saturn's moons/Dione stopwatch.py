import time
from IPython.display import clear_output
print("The solar time model is used for this stopwatch. \n More info here: https://lco.global/spacebook/sky/sidereal-time/"
      " | https://science.nasa.gov/saturn/moons/dione/ | \n https://en.wikipedia.org/wiki/Solar_time | https://en.wikipedia.org/wiki/Synodic_day")
ratio = 2.736915
print(f"A day on Dione, Saturn's moon lasts {ratio} Earth days.")
dioneday = 0
while dioneday <= 365:
    dionehour = 0
    while dionehour < 24:
        dionemins = 0
        while dionemins < 60:
            dionesec = 0
            while dionesec < 60:
                print(f"Dione stopwatch: {dioneday} : {dionehour} : {dionemins} : {dionesec}", end='\x1b[2K')
                time.sleep(ratio)
                clear_output()
                dionesec += 1
            dionemins += 1
        dionehour += 1
    dioneday += 1

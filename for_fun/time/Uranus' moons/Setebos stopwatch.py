import time
from IPython.display import clear_output
print("The solar time model is used for this stopwatch. \n More info here: https://lco.global/spacebook/sky/sidereal-time/"
      " | https://science.nasa.gov/uranus/moons/setebos/ | \n https://en.wikipedia.org/wiki/Solar_time | https://en.wikipedia.org/wiki/Synodic_day")
ratio = 4.255 / 24
print(f"A day on Setebos, Uranus' moon lasts {round(ratio, 8)} Earth days.")
setebosday = 0
while setebosday <= 365:
    seteboshour = 0
    while seteboshour < 24:
        setebosmins = 0
        while setebosmins < 60:
            setebossec = 0
            while setebossec < 60:
                print(f"Setebos stopwatch: {setebosday} : {seteboshour} : {setebosmins} : {setebossec}", end='\x1b[2K')
                time.sleep(ratio)
                clear_output()
                setebossec += 1
            setebosmins += 1
        seteboshour += 1
    setebosday += 1

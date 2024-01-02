import time
from IPython.display import clear_output
print("The solar time model is used for this stopwatch. \n More info here: https://lco.global/spacebook/sky/sidereal-time/"
      " | https://science.nasa.gov/jupiter/facts/ | \n https://en.wikipedia.org/wiki/Solar_time | https://en.wikipedia.org/wiki/Synodic_day")
ratio = 9.9258/24
print(f'A day on Jupiter lasts {ratio} Earth days.')
jday = 0
while jday <= 365:
    jhour = 0
    while jhour < 24:
        jmins = 0
        while jmins < 60:
            jsec = 0
            while jsec < 60:
                print(f"Jupiter stopwatch: {jday} : {jhour} : {jmins} : {jsec}", end='\x1b[2K')
                time.sleep(ratio)
                clear_output()
                jsec += 1
            jmins += 1
        jhour += 1
    jday += 1

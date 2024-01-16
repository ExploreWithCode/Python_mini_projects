import time
from IPython.display import clear_output
print("The solar time model is used for this stopwatch. \n More info here: https://lco.global/spacebook/sky/sidereal-time/"
      " | https://science.nasa.gov/saturn/moons/ijiraq/ | \n https://en.wikipedia.org/wiki/Solar_time | https://en.wikipedia.org/wiki/Synodic_day")
ratio = 13.03 / 24
print(f"A day on Ijiraq, Saturn's moon lasts {round(ratio, 7)} Earth days.")
ijiraqday = 0
while ijiraqday <= 365:
    ijiraqhour = 0
    while ijiraqhour < 24:
        ijiraqmins = 0
        while ijiraqmins < 60:
            ijiraqsec = 0
            while ijiraqsec < 60:
                print(f"Ijiraq stopwatch: {ijiraqday} : {ijiraqhour} : {ijiraqmins} : {ijiraqsec}", end='\x1b[2K')
                time.sleep(ratio)
                clear_output()
                ijiraqsec += 1
            ijiraqmins += 1
        ijiraqhour += 1
    ijiraqday += 1

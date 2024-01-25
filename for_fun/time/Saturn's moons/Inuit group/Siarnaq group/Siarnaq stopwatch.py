import time
from IPython.display import clear_output
print("The solar time model is used for this stopwatch. \n More info here: https://lco.global/spacebook/sky/sidereal-time/"
      " | https://science.nasa.gov/saturn/moons/siarnaq/ | \n https://en.wikipedia.org/wiki/Solar_time | https://en.wikipedia.org/wiki/Synodic_day")
ratio = 10.18785 / 24
print(f"A day on Siarnaq, Saturn's moon lasts {round(ratio, 8)} Earth days.")
siarnaqday = 0
while siarnaqday <= 365:
    siarnaqhour = 0
    while siarnaqhour < 24:
        siarnaqmins = 0
        while siarnaqmins < 60:
            siarnaqsec = 0
            while siarnaqsec < 60:
                print(f"Siarnaq stopwatch: {siarnaqday} : {siarnaqhour} : {siarnaqmins} : {siarnaqsec}", end='\x1b[2K')
                time.sleep(ratio)
                clear_output()
                siarnaqsec += 1
            siarnaqmins += 1
        siarnaqhour += 1
    siarnaqday += 1

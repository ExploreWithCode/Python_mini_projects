import time
from IPython.display import clear_output
print("The solar time model is used for this stopwatch. \n More info here: https://lco.global/spacebook/sky/sidereal-time/"
      " | https://science.nasa.gov/saturn/moons/paaliaq/ | \n https://en.wikipedia.org/wiki/Solar_time | https://en.wikipedia.org/wiki/Synodic_day")
ratio = 18.79 / 24
print(f"A day on Paaliaq, Saturn's moon lasts {round(ratio, 7)} Earth days.")
paaliaqday = 0
while paaliaqday <= 365:
    paaliaqhour = 0
    while paaliaqhour < 24:
        paaliaqmins = 0
        while paaliaqmins < 60:
            paaliaqsec = 0
            while paaliaqsec < 60:
                print(f"Paaliaq stopwatch: {paaliaqday} : {paaliaqhour} : {paaliaqmins} : {paaliaqsec}", end='\x1b[2K')
                time.sleep(ratio)
                clear_output()
                paaliaqsec += 1
            paaliaqmins += 1
        paaliaqhour += 1
    paaliaqday += 1

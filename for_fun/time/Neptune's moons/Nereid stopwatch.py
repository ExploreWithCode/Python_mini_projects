import time
from IPython.display import clear_output
print("The solar time model is used for this stopwatch. \n More info here: https://lco.global/spacebook/sky/sidereal-time/"
      " | https://science.nasa.gov/neptune/moons/nereid/ | \n https://en.wikipedia.org/wiki/Solar_time | https://en.wikipedia.org/wiki/Synodic_day")
ratio = 11.594 / 24
print(f"A day on Nereid, Neptune's moon lasts {round(ratio, 7)} Earth days.")
nereidday = 0
while nereidday <= 365:
    nereidhour = 0
    while nereidhour < 24:
        nereidmins = 0
        while nereidmins < 60:
            nereidsec = 0
            while nereidsec < 60:
                print(f"Nereid stopwatch: {nereidday} : {nereidhour} : {nereidmins} : {nereidsec}", end='\x1b[2K')
                time.sleep(ratio)
                clear_output()
                nereidsec += 1
            nereidmins += 1
        nereidhour += 1
    nereidday += 1

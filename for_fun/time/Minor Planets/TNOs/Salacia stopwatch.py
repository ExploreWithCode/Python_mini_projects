import time
from IPython.display import clear_output
print("The solar time model is used for this stopwatch. \n More info here: https://lco.global/spacebook/sky/sidereal-time/"
      " | https://en.wikipedia.org/wiki/120347_Salacia | \n https://en.wikipedia.org/wiki/Solar_time | https://en.wikipedia.org/wiki/Synodic_day")
ratio = 6.09 / 24
print(f'A day on Salacia, a minor planet, lasts {ratio} Earth days.')
salaciaday = 0
while salaciaday <= 365:
    salaciahour = 0
    while salaciahour < 24:
        salaciamins = 0
        while salaciamins < 60:
            salaciasec = 0
            while salaciasec < 60:
                print(f"Salacia stopwatch: {salaciaday} : {salaciahour} : {salaciamins} : {salaciasec}", end='\x1b[2K')
                time.sleep(ratio)
                clear_output()
                salaciasec += 1
            salaciamins += 1
        salaciahour += 1
    salaciaday += 1

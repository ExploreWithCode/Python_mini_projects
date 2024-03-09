import time
from IPython.display import clear_output
print("The solar time model is used for this stopwatch. \n More info here: https://lco.global/spacebook/sky/sidereal-time/"
      " | https://en.wikipedia.org/wiki/225088_varda | \n https://en.wikipedia.org/wiki/Solar_time | https://en.wikipedia.org/wiki/Synodic_day")
ratio1 = 5.61 / 24
ratio2 = 5.91 / 24
ratio3 = 11.82 / 24
print(f"A day on Varda, a planetoid lasts this many Earth days:\n"
      f"single-peaked scenario 1: {ratio1}\n"
      f"single-peaked scenario 2: {ratio2}\n"
      f"double-peaked: {ratio3}\n")
inp = input("Pick a scenario: '1' for single-peaked scenario 1, '2' for single-peaked scenario 2 or '3' for double-peaked\n")
if inp == "1":
    vardaday = 0
    while vardaday <= 365:
        vardahour = 0
        while vardahour < 24:
            vardamins = 0
            while vardamins < 60:
                vardasec = 0
                while vardasec < 60:
                    print(f"Varda stopwatch: {vardaday} : {vardahour} : {vardamins} : {vardasec}", end='\x1b[2K')
                    time.sleep(ratio1)
                    clear_output()
                    vardasec += 1
                vardamins += 1
            vardahour += 1
        vardaday += 1
elif inp == "2":
    vardaday = 0
    while vardaday <= 365:
        vardahour = 0
        while vardahour < 24:
            vardamins = 0
            while vardamins < 60:
                vardasec = 0
                while vardasec < 60:
                    print(f"Varda stopwatch: {vardaday} : {vardahour} : {vardamins} : {vardasec}", end='\x1b[2K')
                    time.sleep(ratio2)
                    clear_output()
                    vardasec += 1
                vardamins += 1
            vardahour += 1
        vardaday += 1
elif inp == "3":
    vardaday = 0
    while vardaday <= 365:
        vardahour = 0
        while vardahour < 24:
            vardamins = 0
            while vardamins < 60:
                vardasec = 0
                while vardasec < 60:
                    print(f"Varda stopwatch: {vardaday} : {vardahour} : {vardamins} : {vardasec}", end='\x1b[2K')
                    time.sleep(ratio3)
                    clear_output()
                    vardasec += 1
                vardamins += 1
            vardahour += 1
        vardaday += 1
else:
    print("Wrong number!")

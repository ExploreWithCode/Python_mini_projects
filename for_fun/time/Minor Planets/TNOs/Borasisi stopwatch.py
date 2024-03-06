import time
from IPython.display import clear_output
print("The solar time model is used for this stopwatch. \n More info here: https://lco.global/spacebook/sky/sidereal-time/"
      " | https://en.wikipedia.org/wiki/66652_Borasisi | \n https://en.wikipedia.org/wiki/Solar_time | https://en.wikipedia.org/wiki/Synodic_day")
ratio = 6.4 / 24
print(f'A day on Borasisi, a cubewano, lasts {ratio} Earth days.')
borasisiday = 0
while borasisiday <= 365:
    borasisihour = 0
    while borasisihour < 24:
        borasisimins = 0
        while borasisimins < 60:
            borasisisec = 0
            while borasisisec < 60:
                print(f"Borasisi stopwatch: {borasisiday} : {borasisihour} : {borasisimins} : {borasisisec}", end='\x1b[2K')
                time.sleep(ratio)
                clear_output()
                borasisisec += 1
            borasisimins += 1
        borasisihour += 1
    borasisiday += 1

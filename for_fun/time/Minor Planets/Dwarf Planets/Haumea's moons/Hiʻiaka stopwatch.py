import time
from IPython.display import clear_output
print("The solar time model is used for this stopwatch. \n More info here: https://lco.global/spacebook/sky/sidereal-time/"
      " | https://en.wikipedia.org/wiki/Hiʻiaka_(moon) | \n https://en.wikipedia.org/wiki/Solar_time | https://en.wikipedia.org/wiki/Synodic_day")
ratio = 9.8 / 24
print(f'A day on Hiʻiaka, a moon of the dwarf planet Haumea, lasts {round(ratio, 5)} Earth days.')
hiiakaday = 0
while hiiakaday <= 365:
    hiiakahour = 0
    while hiiakahour < 24:
        hiiakamins = 0
        while hiiakamins < 60:
            hiiakasec = 0
            while hiiakasec < 60:
                print(f"Hiʻiaka stopwatch: {hiiakaday} : {hiiakahour} : {hiiakamins} : {hiiakasec}", end='\x1b[2K')
                time.sleep(ratio)
                clear_output()
                hiiakasec += 1
            hiiakamins += 1
        hiiakahour += 1
    hiiakaday += 1

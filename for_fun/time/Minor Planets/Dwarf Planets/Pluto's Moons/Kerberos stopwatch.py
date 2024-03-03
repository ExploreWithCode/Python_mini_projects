import time
from IPython.display import clear_output
print("The solar time model is used for this stopwatch. \n More info here: https://lco.global/spacebook/sky/sidereal-time/"
      " | https://en.wikipedia.org/wiki/Kerberos_(moon) | \n https://en.wikipedia.org/wiki/Solar_time | https://en.wikipedia.org/wiki/Synodic_day")
ratio = 5.31 / 24
print(f'A day on Kerberos, a moon of the dwarf planet Pluto, lasts {round(ratio, 5)} Earth days.')
kerberosday = 0
while kerberosday <= 365:
    kerberoshour = 0
    while kerberoshour < 24:
        kerberosmins = 0
        while kerberosmins < 60:
            kerberossec = 0
            while kerberossec < 60:
                print(f"Kerberos stopwatch: {kerberosday} : {kerberoshour} : {kerberosmins} : {kerberossec}", end='\x1b[2K')
                time.sleep(ratio)
                clear_output()
                kerberossec += 1
            kerberosmins += 1
        kerberoshour += 1
    kerberosday += 1

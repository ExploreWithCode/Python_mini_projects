# Exceptions are not included
year = int(input('year = '))

if year%400 == 0 or year%4 == 0:
    leap_year = True
else:
    leap_year = False

print(leap_year)

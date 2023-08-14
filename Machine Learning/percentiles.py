import numpy
ages = [5, 31, 43, 48, 50, 41, 7, 11, 15, 39, 80, 82, 32, 2, 8, 6, 25, 36, 27, 61]
print("What percentage of the values do you want to be lower than the output value?\n"
      "Give me a number (without '%'): ")
inp = int(input())
x = numpy.percentile(ages, inp)
if max(ages) == x:
    print(f"{inp}% of the values are lower than or equal to {x}")
else:
    print(f"{inp}% of the values are lower than {x}")

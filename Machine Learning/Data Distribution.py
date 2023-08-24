from statistics import mode
import numpy
import matplotlib.pyplot as plt
print("Give me the minimum value: ")
low = int(input())
print("Give me the maximum value: ")
high = int(input())
print("Give me the value size: ")
size = int(input())
x = numpy.random.uniform(low, high, size)

md = mode(x)  # most common (in case of a tie, the first value is printed)
print(f"Mode: {round(md, 2)}")

if size < 10:
    plt.hist(x, size)
elif size < 100:
    plt.hist(x, 10)
else:
    plt.hist(x, 100)
plt.show()

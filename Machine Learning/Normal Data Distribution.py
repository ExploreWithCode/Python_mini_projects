from statistics import mode
import numpy
import matplotlib.pyplot as plt
print("Give me the average value: ")
mean = int(input())
print("Give me the standard deviation: ")
std = int(input())
print("Give me the value size: ")
size = int(input())
x = numpy.random.normal(mean, std, size)

mn = min(x)
mx = max(x)
md = mode(x)  # most common (in case of a tie, the first value is printed)
mn_d = mean - min(x)  # deviation of the minimum value
mx_d = max(x) - mean  # deviation of the maximum value
mxd = max(mn_d, mx_d)  # maximum deviation from the average
print(f"MIN: {round(mn, 2)} | MAX: {round(mx, 2)}\nMode: {round(md, 2)} | Maximum deviation: {round(mxd, 2)}")

if size < 10:
    plt.hist(x, size)
elif size < 100:
    plt.hist(x, 10)
else:
    plt.hist(x, 100)
plt.show()

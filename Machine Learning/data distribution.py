import numpy
import matplotlib.pyplot as plt
print("Give me the minimum value: ")
low = int(input())
print("Give me the maximum value: ")
high = int(input())
print("Give me the value size: ")
size = int(input())
x = numpy.random.uniform(low, high, size)
print(x)
plt.hist(x, size)
plt.show()

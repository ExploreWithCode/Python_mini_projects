import numpy
import matplotlib.pyplot as plt
print("DATA SET 1")
print("Give me the average value: ")
mean = int(input())
print("Give me the standard deviation: ")
std = int(input())
print("Give me the value size: ")
size = int(input())
x = numpy.random.normal(mean, std, size)

print("DATA SET 2")
print("Give me the average value: ")
mean2 = int(input())
print("Give me the standard deviation: ")
std2 = int(input())
y = numpy.random.normal(mean2, std2, size)

plt.scatter(x, y)
plt.show()

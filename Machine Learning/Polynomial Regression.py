import numpy
import matplotlib.pyplot as plt
from sklearn.metrics import r2_score

print("DATA SET 1")
print("Give me the minimum value: ")
low = int(input())
print("Give me the maximum value: ")
high = int(input())
size = 20
x = numpy.random.uniform(low, high, size)

print("\nDATA SET 2")
print("Give me the minimum value: ")
low2 = int(input())
print("Give me the maximum value: ")
high2 = int(input())
y = numpy.random.uniform(low2, high2, size)

mymodel = numpy.poly1d(numpy.polyfit(x, y, 3))

myline = numpy.linspace(low, high, 100)

print("Give me a value on the 'x' axis to predict the corresponding value on the 'y' axis: ")
v = int(input())
pv = mymodel(v)
print(f"The predicted value is {round(pv, 2)}.")

print(f"The relationship between the values on the two axes is {round(r2_score(y, mymodel(x)), 2)}.")

plt.scatter(x, y)
plt.plot(myline, mymodel(myline))
plt.show()

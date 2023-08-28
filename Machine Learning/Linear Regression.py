import matplotlib.pyplot as plt
import numpy
from scipy import stats

print("DATA SET 1")
print("Give me the minimum value: ")
low = int(input())
print("Give me the maximum value: ")
high = int(input())
size = 20
x = numpy.random.uniform(low, high, size)

print("DATA SET 2")
print("Give me the minimum value: ")
low2 = int(input())
print("Give me the maximum value: ")
high2 = int(input())
y = numpy.random.uniform(low2, high2, size)

slope, intercept, r, p, std_err = stats.linregress(x, y)


def myfunc(x):
  return slope * x + intercept


print("Give me a value on the 'x' axis to predict the corresponding value on the 'y' axis: ")
v = int(input())
pv = myfunc(v)
print(f"The predicted value is {round(pv, 2)}.")

mymodel = list(map(myfunc, x))

print(f"The correlation between the values on the two axes is {round(r, 2)}.")

plt.scatter(x, y)
plt.plot(x, mymodel)
plt.show()

from statistics import mode
import numpy
print("Give me the 1st value: ")
v1 = float(input())
print("Give me the 2nd value: ")
v2 = float(input())
print("Give me the 3rd value: ")
v3 = float(input())
print("Give me the 4th value: ")
v4 = float(input())
print("Give me the 5th value: ")
v5 = float(input())
print("Give me the 6th value: ")
v6 = float(input())
values = [v1, v2, v3, v4, v5, v6]

avg = round(numpy.mean(values), 2)  # mean = average
mdn = round(numpy.median(values), 2)  # median = middle value
md = round(mode(values), 2)  # most common (in case of a tie, the first value is printed)
std = round(numpy.std(values), 2)  # standard deviation
mx_d = round(max(values) - avg, 2)  # deviation of the maximum value
mn_d = round(avg - min(values), 2)  # deviation of the minimum value
mxd = max(mn_d, mx_d)  # maximum deviation from the average

dlist = []
for n in values:
    dif = abs(n - avg)
    dlist.append(dif)
    mnd = round(min(dlist), 2)  # minimum deviation from the average
print(f"Mean: {avg} | Median: {mdn} | Mode: {md}")
print(f"Standard deviation: {std} | Maximum deviation: {mxd} | Minimum deviation: {mnd}")

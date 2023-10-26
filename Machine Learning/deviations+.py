from statistics import mode
import numpy
values = []
brk = ["N", "n"]
while True:
    print("Enter a number:")
    vlpre = input()
    if vlpre.isnumeric():
        vl = float(vlpre)
        values.append(vl)
        conf = input("Press anything to continue or 'N' to stop adding numbers. ")
        if conf in brk:
            break
    else:
        print("Invalid input!")
print(f"Values: {values}")

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

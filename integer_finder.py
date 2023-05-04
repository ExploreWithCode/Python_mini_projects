accepted_replies = ["yes", "y", "YES", "Y", "Yes"]
print("This tool helps you find all the integers between (and excluding) two given numbers.")
min = int(input("Insert the minimum number:"))
max = int(input("Insert the maximum number:"))
choice = input("Do you want these numbers to be included in the result?")
if min >= max:
    print("The minimum number has to be smaller than the maximum!")
print("The numbers you requested are these:")
if choice in accepted_replies:
    while min <= max:
        print(min, end=" ")
        min += 1
else:
    if max - min <= 1:
        print("If the distance between the minimum and the maximum is not bigger than 1, no number gets printed.")
    while min < max - 1:
        min += 1
        print(min, end=" ")


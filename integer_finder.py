accepted_replies = ["yes", "y", "YES", "Y", "Yes"]
print("This tool helps you find all the integers between (and excluding) two given numbers.")
i = int(input("Insert the initial number:"))
m = int(input("Insert the maximum number:"))
choice = input("Do you want these numbers to be included in the result?")
if i >= m:
    print("The initial number has to be smaller than the maximum!")
print("The numbers you requested are these:")
if choice in accepted_replies:
    while i <= m:
        print(i, end=" ")
        i += 1
else:
    if m - i <= 1:
        print("If the distance between the initial and the maximum is not bigger than 1, no number gets printed.")
    while i < m - 1:
        i += 1
        print(i, end=" ")
       

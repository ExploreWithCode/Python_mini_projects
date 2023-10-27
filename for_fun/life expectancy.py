females = float(76.0)
males = float(70.8)
both = round((females+males)/2, 2) # more at https://www.worldometers.info/demographics/life-expectancy/
print("The average life expectancy of a human in general right now is", both, "years.")
print("Enter your age: ")
age = input()
per_of_both = (int(age)/int(both)*100)
per_of_females = (int(age)/int(females)*100)
per_of_males = (int(age)/int(males)*100)
if int(age) < 0:
    print("Pick a valid number!")
else:
    print("You have lived this percentage of your expected life according to worldwide data for:")
    print("both sexes :", round(per_of_both, 2), "%")
    print("females :", round(per_of_females, 2), "%")
    print("males :", round(per_of_males, 2), "%")

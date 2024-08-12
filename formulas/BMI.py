print("Body Mass Index (BMI) is a simple way to have a quick estimate of your body fat category.")

def get_valid_number(prompt):
    while True:
        user_input = input(prompt)
        if user_input.replace(".", "", 1).isdigit():
            value = float(user_input)
            if value > 0:
                return value
            else:
                print("Please enter a positive number!")
        else:
            print("That's not a valid answer. Please try again!")

def get_valid_units():
    while True:
        units_q = input("Choose either 'metric' or 'US' units: ").lower()
        if units_q == "metric" or units_q == "us":
            return units_q
        else:
            print("Sorry, I didn't understand that. Please choose either 'metric' or 'US' units.")

units_q = get_valid_units()

def bmi_calculator(weight, height, factor=1):
    return weight / pow(height, 2) * factor

if units_q == "metric":
    weight = get_valid_number("Give me your weight in kg: ")
    height = get_valid_number("Give me your height in m: ")
    bmi = bmi_calculator(weight, height)
elif units_q == "us":
    weight = get_valid_number("Give me your weight in lb: ")
    height = get_valid_number("Give me your height in inches: ")
    bmi = bmi_calculator(weight, height, 703)

categories = {
    "Underweight": (bmi, 18.5),
    "Normal weight": (18.5, 24.9),
    "Overweight": (25, 29.9),
    "Obese": (30, float("inf"))
}

for category, (lower, upper) in categories.items():
    if lower <= bmi < upper:
        print(f"With a score of {round(bmi, 2)}, you are in the category: '{category}'.")
        break

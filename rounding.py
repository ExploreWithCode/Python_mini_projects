# Customized rounding of a number
num = float(input("Give me a number to round: "))
r_n = int(input("By how many decimals do you want to round up the number you gave me? "))
rounded = round(num, r_n)
print(rounded)

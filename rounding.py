# Customized rounding of a number
brk = ["N", "n"]
asdf = ""
while asdf is not brk:
    num = float(input("Give me a number to round: "))
    r_n = int(input("By how many decimals do you want to round up the number you gave me? "))
    rounded = round(num, r_n)
    print(rounded)
    conf = input("Press anything to continue or 'N' to stop adding numbers. ")
    if conf in brk:
        break

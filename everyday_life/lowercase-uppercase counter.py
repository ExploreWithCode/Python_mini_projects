def cnt(text):
    lowercase = 0
    uppercase = 0
    for char in text:
        if char.isalpha():
            if char.islower():
                lowercase += 1
            else:
                uppercase += 1
    lowc = ("Lowercase:", lowercase)
    upc = ("Uppercase:", uppercase)
    print("Lowercase:", lowercase)
    print("Uppercase:", uppercase)
    return ""


inp = cnt(input("Type something: \n"))
print(inp)

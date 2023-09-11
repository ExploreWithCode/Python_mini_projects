def count(text):
    lowercase = 0
    uppercase = 0
    for char in text:
        if char.isalpha():
            if char.islower():
                lowercase += 1
            else:
                uppercase += 1
    return lowercase, uppercase


inp = count(input("Type something: \n"))
print(inp)

inp = input("Enter a letter (uppercase or lowercase) and receive its order in the alphabet:\n")
alphabet = "abcdefghijklmnopqrstuvwxyz"


def func(txt):
    val = 0
    if not txt.isalpha():
        print("Give me a letter!")
    elif len(txt) != 1:
        print("Give only ONE letter!")
    txt = txt.lower()
    for char in alphabet:
        if txt == char:
            val = alphabet.index(char) + 1
    return val


if func(inp) > 0:
    print(f"\"{inp}\" has the value of {func(inp)}.")

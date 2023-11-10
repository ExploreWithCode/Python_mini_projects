inp = input("Enter a letter (uppercase or lowercase) and receive its order in the alphabet:\n")
inp = inp.lower()
alphabet = "abcdefghijklmnopqrstuvwxyz"


def func(txt):
    t = True
    while t:
        if not txt.isalpha() or txt not in alphabet:
            txt = input('Type a letter from the English alphabet:\n')
        elif len(txt) != 1:
            txt = input('Type no more or less than 1 character:\n')
        else:
            t = False
    for char in alphabet:
        if txt == char:
            val = alphabet.index(char) + 1
            print(f"\"{txt}\" has the value of {val}.")
            break
    return ''


func(inp)

letters = "abcdefghijklmnopqrstuvwxyz"
en_key = 1


def invert(phrase):
    inversion = ""
    for letter in phrase:
        if letter.isupper():
            inversion = inversion + letter.lower()  # turn uppercase into lowercase
        else:
            inversion = inversion + letter.upper()  # turn lowercase into uppercase
    return inversion


print(invert(input("I will turn uppercase into lowercase and vise versa. Type something: ")))

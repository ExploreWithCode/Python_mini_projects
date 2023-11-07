inp = input("Enter a letter (uppercase or lowercase) and receive its order in the alphabet:\n")
inp = inp.lower()
alphabet = list("abcdefghijklmnopqrstuvwxyz")
for index, ch in enumerate(alphabet):
    if inp == ch:
        print(ch, '=', index+1)

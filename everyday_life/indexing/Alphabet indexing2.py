inp = input("Enter one letter (without spaces) and receive its order in the alphabet:\n")
inp = inp.lower()
alphabet = list("abcdefghijklmnopqrstuvwxyz")
t = True
while t:
    if not inp.isalpha() or inp not in alphabet:
        inp = input('Type a letter from the English alphabet:\n')
    elif len(inp) != 1:
        inp = input('Type no more or less than 1 character:\n')
    else:
        t = False

for index, ch in enumerate(alphabet):
    if inp == ch:
        print(ch, '=', index+1)

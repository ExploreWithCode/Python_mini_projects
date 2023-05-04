letters = "abcdefghijklmnopqrstuvwxyz"
en_key = 1
def encrypt(phrase):
    encryption = ""
    for letter in phrase:
        if letter.lower() == letters[0] in letters: # a
            if letter.isupper():
                encryption = encryption + letters.upper()[0 + en_key]
            else:
                encryption = encryption + letters[0 + en_key]
        elif letter.lower() == letters[1] in letters: # b
            if letter.isupper():
                encryption = encryption + letters.upper()[1 + en_key]
            else:
                encryption = encryption + letters[1 + en_key]
        elif letter.lower() == letters[2] in letters: # c
            if letter.isupper():
                encryption = encryption + letters.upper()[2 + en_key]
            else:
                encryption = encryption + letters[2 + en_key]
        elif letter.lower() == letters[3] in letters: # d
            if letter.isupper():
                encryption = encryption + letters.upper()[3 + en_key]
            else:
                encryption = encryption + letters[3 + en_key]
        elif letter.lower() == letters[4] in letters: # e
            if letter.isupper():
                encryption = encryption + letters.upper()[4 + en_key]
            else:
                encryption = encryption + letters[4 + en_key]
        elif letter.lower() == letters[5] in letters: # f
            if letter.isupper():
                encryption = encryption + letters.upper()[5 + en_key]
            else:
                encryption = encryption + letters[5 + en_key]
        elif letter.lower() == letters[6] in letters: # g
            if letter.isupper():
                encryption = encryption + letters.upper()[6 + en_key]
            else:
                encryption = encryption + letters[6 + en_key]
        elif letter.lower() == letters[7] in letters: # h
            if letter.isupper():
                encryption = encryption + letters.upper()[7 + en_key]
            else:
                encryption = encryption + letters[7 + en_key]
        elif letter.lower() == letters[8] in letters: # i
            if letter.isupper():
                encryption = encryption + letters.upper()[8 + en_key]
            else:
                encryption = encryption + letters[8 + en_key]
        elif letter.lower() == letters[9] in letters: # j
            if letter.isupper():
                encryption = encryption + letters.upper()[9 + en_key]
            else:
                encryption = encryption + letters[9 + en_key]
        elif letter.lower() == letters[10] in letters: # k
            if letter.isupper():
                encryption = encryption + letters.upper()[10 + en_key]
            else:
                encryption = encryption + letters[10 + en_key]
        elif letter.lower() == letters[11] in letters: # l
            if letter.isupper():
                encryption = encryption + letters.upper()[11 + en_key]
            else:
                encryption = encryption + letters[11 + en_key]
        elif letter.lower() == letters[12] in letters: # m
            if letter.isupper():
                encryption = encryption + letters.upper()[12 + en_key]
            else:
                encryption = encryption + letters[12 + en_key]
        elif letter.lower() == letters[13] in letters: # n
            if letter.isupper():
                encryption = encryption + letters.upper()[13 + en_key]
            else:
                encryption = encryption + letters[13 + en_key]
        elif letter.lower() == letters[14] in letters: # o
            if letter.isupper():
                encryption = encryption + letters.upper()[14 + en_key]
            else:
                encryption = encryption + letters[14 + en_key]
        elif letter.lower() == letters[15] in letters: # p
            if letter.isupper():
                encryption = encryption + letters.upper()[15 + en_key]
            else:
                encryption = encryption + letters[15 + en_key]
        elif letter.lower() == letters[16] in letters: # q
            if letter.isupper():
                encryption = encryption + letters.upper()[16 + en_key]
            else:
                encryption = encryption + letters[16 + en_key]
        elif letter.lower() == letters[17] in letters: # r
            if letter.isupper():
                    encryption = encryption + letters.upper()[17 + en_key]
            else:
                encryption = encryption + letters[17 + en_key]
        elif letter.lower() == letters[18] in letters: # s
            if letter.isupper():
                encryption = encryption + letters.upper()[18 + en_key]
            else:
                encryption = encryption + letters[18 + en_key]
        elif letter.lower() == letters[19] in letters: # t
            if letter.isupper():
                encryption = encryption + letters.upper()[19 + en_key]
            else:
                encryption = encryption + letters[19 + en_key]
        elif letter.lower() == letters[20] in letters: # u
            if letter.isupper():
                encryption = encryption + letters.upper()[20 + en_key]
            else:
                encryption = encryption + letters[20 + en_key]
        elif letter.lower() == letters[21] in letters: # v
            if letter.isupper():
                encryption = encryption + letters.upper()[21 + en_key]
            else:
                encryption = encryption + letters[21 + en_key]
        elif letter.lower() == letters[22] in letters: # w
            if letter.isupper():
                encryption = encryption + letters.upper()[22 + en_key]
            else:
                encryption = encryption + letters[22 + en_key]
        elif letter.lower() == letters[23] in letters: # x
            if letter.isupper():
                encryption = encryption + letters.upper()[23 + en_key]
            else:
                encryption = encryption + letters[23 + en_key]
        elif letter.lower() == letters[24] in letters: # y
            if letter.isupper():
                encryption = encryption + letters.upper()[24 + en_key]
            else:
                encryption = encryption + letters[24 + en_key]
        elif letter.lower() == letters[25] in letters: # z
            if letter.isupper():
                encryption = encryption + letters.upper()[-1 + en_key]
            else:
                encryption = encryption + letters[-1 + en_key]
        else:
            encryption = encryption + letter
    return encryption


print(encrypt(input("Enter a phrase to modify: ")))

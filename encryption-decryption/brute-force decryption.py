def decrypt(text):
    result = result_2 = result_3 = result_4 = result_5 = result_6 = result_7 = result_8 = result_9 = result_10 = \
        result_11 = result_12 = result_13 = result_14 = result_15 = result_16 = result_17 = result_18 = result_19 = \
        result_20 = result_21 = result_22 = result_23 = result_24 = result_25 = result_26 = ""
    for char in text:
        if char.isalpha():
            alphabet = 'abcdefghijklmnopqrstuvwxyz' if char.islower() else 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
            shifted = alphabet[(alphabet.index(char)-1) % 26]
            result += shifted
            shifted_2 = alphabet[(alphabet.index(char)-2) % 26]
            result_2 += shifted_2
            shifted_3 = alphabet[(alphabet.index(char)-3) % 26]
            result_3 += shifted_3
            shifted_4 = alphabet[(alphabet.index(char)-4) % 26]
            result_4 += shifted_4
            shifted_5 = alphabet[(alphabet.index(char)-5) % 26]
            result_5 += shifted_5
            shifted_6 = alphabet[(alphabet.index(char)-6) % 26]
            result_6 += shifted_6
            shifted_7 = alphabet[(alphabet.index(char)-7) % 26]
            result_7 += shifted_7
            shifted_8 = alphabet[(alphabet.index(char)-8) % 26]
            result_8 += shifted_8
            shifted_9 = alphabet[(alphabet.index(char)-9) % 26]
            result_9 += shifted_9
            shifted_10 = alphabet[(alphabet.index(char)-10) % 26]
            result_10 += shifted_10
            shifted_11 = alphabet[(alphabet.index(char)-11) % 26]
            result_11 += shifted_11
            shifted_12 = alphabet[(alphabet.index(char)-12) % 26]
            result_12 += shifted_12
            shifted_13 = alphabet[(alphabet.index(char)-13) % 26]
            result_13 += shifted_13
            shifted_14 = alphabet[(alphabet.index(char)-14) % 26]
            result_14 += shifted_14
            shifted_15 = alphabet[(alphabet.index(char)-15) % 26]
            result_15 += shifted_15
            shifted_16 = alphabet[(alphabet.index(char)-16) % 26]
            result_16 += shifted_16
            shifted_17 = alphabet[(alphabet.index(char)-17) % 26]
            result_17 += shifted_17
            shifted_18 = alphabet[(alphabet.index(char)-18) % 26]
            result_18 += shifted_18
            shifted_19 = alphabet[(alphabet.index(char)-19) % 26]
            result_19 += shifted_19
            shifted_20 = alphabet[(alphabet.index(char)-20) % 26]
            result_20 += shifted_20
            shifted_21 = alphabet[(alphabet.index(char)-21) % 26]
            result_21 += shifted_21
            shifted_22 = alphabet[(alphabet.index(char)-22) % 26]
            result_22 += shifted_22
            shifted_23 = alphabet[(alphabet.index(char)-23) % 26]
            result_23 += shifted_23
            shifted_24 = alphabet[(alphabet.index(char)-24) % 26]
            result_24 += shifted_24
            shifted_25 = alphabet[(alphabet.index(char)-25) % 26]
            result_25 += shifted_25
            shifted_26 = alphabet[(alphabet.index(char)-26) % 26]
            result_26 += shifted_26
        else:
            result += char
            result_2 += char
            result_3 += char
            result_4 += char
            result_5 += char
            result_6 += char
            result_7 += char
            result_8 += char
            result_9 += char
            result_10 += char
            result_11 += char
            result_12 += char
            result_13 += char
            result_14 += char
            result_15 += char
            result_16 += char
            result_17 += char
            result_18 += char
            result_19 += char
            result_20 += char
            result_21 += char
            result_22 += char
            result_23 += char
            result_24 += char
            result_25 += char
            result_26 += char
    return result, result_2, result_3, result_4, result_5, result_6, result_7, result_8, result_9, result_10,\
        result_11, result_12, result_13, result_14, result_15, result_16, result_17, result_18, result_19, result_20,\
        result_21, result_22, result_23, result_24, result_25, result_26


def decrypt_rev(text):
    result = result_2 = result_3 = result_4 = result_5 = result_6 = result_7 = result_8 = result_9 = result_10 = \
        result_11 = result_12 = result_13 = result_14 = result_15 = result_16 = result_17 = result_18 = result_19 = \
        result_20 = result_21 = result_22 = result_23 = result_24 = result_25 = result_26 = ""
    for char in text:
        if char.isalpha():
            alphabet = 'abcdefghijklmnopqrstuvwxyz' if char.islower() else 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
            shifted = alphabet[(alphabet.index(char)-1) % 26]
            result += shifted
            shifted_2 = alphabet[(alphabet.index(char)-2) % 26]
            result_2 += shifted_2
            shifted_3 = alphabet[(alphabet.index(char)-3) % 26]
            result_3 += shifted_3
            shifted_4 = alphabet[(alphabet.index(char)-4) % 26]
            result_4 += shifted_4
            shifted_5 = alphabet[(alphabet.index(char)-5) % 26]
            result_5 += shifted_5
            shifted_6 = alphabet[(alphabet.index(char)-6) % 26]
            result_6 += shifted_6
            shifted_7 = alphabet[(alphabet.index(char)-7) % 26]
            result_7 += shifted_7
            shifted_8 = alphabet[(alphabet.index(char)-8) % 26]
            result_8 += shifted_8
            shifted_9 = alphabet[(alphabet.index(char)-9) % 26]
            result_9 += shifted_9
            shifted_10 = alphabet[(alphabet.index(char)-10) % 26]
            result_10 += shifted_10
            shifted_11 = alphabet[(alphabet.index(char)-11) % 26]
            result_11 += shifted_11
            shifted_12 = alphabet[(alphabet.index(char)-12) % 26]
            result_12 += shifted_12
            shifted_13 = alphabet[(alphabet.index(char)-13) % 26]
            result_13 += shifted_13
            shifted_14 = alphabet[(alphabet.index(char)-14) % 26]
            result_14 += shifted_14
            shifted_15 = alphabet[(alphabet.index(char)-15) % 26]
            result_15 += shifted_15
            shifted_16 = alphabet[(alphabet.index(char)-16) % 26]
            result_16 += shifted_16
            shifted_17 = alphabet[(alphabet.index(char)-17) % 26]
            result_17 += shifted_17
            shifted_18 = alphabet[(alphabet.index(char)-18) % 26]
            result_18 += shifted_18
            shifted_19 = alphabet[(alphabet.index(char)-19) % 26]
            result_19 += shifted_19
            shifted_20 = alphabet[(alphabet.index(char)-20) % 26]
            result_20 += shifted_20
            shifted_21 = alphabet[(alphabet.index(char)-21) % 26]
            result_21 += shifted_21
            shifted_22 = alphabet[(alphabet.index(char)-22) % 26]
            result_22 += shifted_22
            shifted_23 = alphabet[(alphabet.index(char)-23) % 26]
            result_23 += shifted_23
            shifted_24 = alphabet[(alphabet.index(char)-24) % 26]
            result_24 += shifted_24
            shifted_25 = alphabet[(alphabet.index(char)-25) % 26]
            result_25 += shifted_25
            shifted_26 = alphabet[(alphabet.index(char)-26) % 26]
            result_26 += shifted_26
        else:
            result += char
            result_2 += char
            result_3 += char
            result_4 += char
            result_5 += char
            result_6 += char
            result_7 += char
            result_8 += char
            result_9 += char
            result_10 += char
            result_11 += char
            result_12 += char
            result_13 += char
            result_14 += char
            result_15 += char
            result_16 += char
            result_17 += char
            result_18 += char
            result_19 += char
            result_20 += char
            result_21 += char
            result_22 += char
            result_23 += char
            result_24 += char
            result_25 += char
            result_26 += char
    return result[::-1], result_2[::-1], result_3[::-1], result_4[::-1], result_5[::-1], result_6[::-1],\
        result_7[::-1], result_8[::-1], result_9[::-1], result_10[::-1], result_11[::-1], result_12[::-1],\
        result_13[::-1], result_14[::-1], result_15[::-1], result_16[::-1], result_17[::-1], result_18[::-1],\
        result_19[::-1], result_20[::-1], result_21[::-1], result_22[::-1], result_23[::-1], result_24[::-1],\
        result_25[::-1], result_26[::-1]


vls = []
brk = ["N", "n"]
asdf = ""
while asdf is not brk:
    res2 = input("Enter the text you want to decrypt: \n")
    print(f"Decryption attempts: {decrypt(res2)}")
    accepted_replies = ["yes", "y", "YES", "Y", "Yes"]
    answer = input(f"Do you want to flip the result? | Accepted replies: {accepted_replies} \n")
    if answer in accepted_replies:
        print(decrypt_rev(res2))
    else:
        print("The result will not be flipped.")
    conf = input("Press anything to continue or 'N' to stop decrypting. ")
    if conf in brk:
        break

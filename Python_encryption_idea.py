# my code is similar but more condensed. If you'd like to pull it apart to make it readable please do so
# it basically hinges on using two alphabets and switching between them based on the character rather than
# using multiple if statements to check.

en_key = 1

def encrypt(text):
    result = ""
    for char in text:
        if char.isalpha():
            alphabet = 'abcdefghijklmnopqrstuvwxyz' if char.islower() else 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
            shifted = alphabet[(alphabet.index(char) + en_key) % 26]
            result += shifted
        else:
            result += char
    return result

print(encrypt(input("Enter a phrase to modify: ")))
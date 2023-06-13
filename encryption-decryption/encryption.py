import keys


def encrypt(text):
    result = ""
    for char in text:
        if char.isalpha():
            alphabet = 'abcdefghijklmnopqrstuvwxyz' if char.islower() else 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
            shifted = alphabet[(alphabet.index(char) + pow(keys.en_key, keys.en_key2) + (keys.en_key + keys.en_key2)*2) % 26]
            result += shifted
        else:
            result += char
    return result[::-1]  # reversal of string


res = encrypt(input("Enter the text you want to encrypt: \n"))  # encryption
print(f"Encrypted message: {res}")

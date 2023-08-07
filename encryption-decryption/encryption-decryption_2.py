en_key = 1
enk = input("Type something and I will use it to encrypt the next text: \n")
en_key2 = len(enk)


def encrypt(text):
    result = ""
    for char in text:
        if char.isalpha():
            if char.islower():
                alphabet = 'abcdefghijklmnopqrstuvwxyz'
                shifted = alphabet[(alphabet.index(char) + pow(en_key, en_key2) + (en_key + en_key2)*2) % 26]
            else:
                alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
                shifted = alphabet[(alphabet.index(char) + pow(en_key, en_key2) + (en_key + en_key2 + 1)*2) % 26]
            result += shifted
        elif char.isnumeric():
            numbers = '1234567890'
            shifted = numbers[(numbers.index(char) + pow(en_key, en_key2) + (en_key + en_key2 + 2)*2) % 10]
            result += shifted
        else:
            result += char
    return result[::-1]  # reversal of string


res = encrypt(input("Enter the text you want to encrypt: \n"))  # encryption
print(f"Encrypted message: {res}")


def decrypt(text):
    result = ""
    for char in text:
        if char.isalpha():
            if char.islower():
                alphabet = 'abcdefghijklmnopqrstuvwxyz'
                shifted = alphabet[(alphabet.index(char) - pow(en_key, en_key2) - (en_key + en_key2)*2) % 26]
            else:
                alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
                shifted = alphabet[(alphabet.index(char) - pow(en_key, en_key2) - (en_key + en_key2 + 1)*2) % 26]
            result += shifted
        elif char.isnumeric():
            numbers = '1234567890'
            shifted = numbers[(numbers.index(char) - pow(en_key, en_key2) - (en_key + en_key2 + 2)*2) % 10]
            result += shifted
        else:
            result += char
    return result[::-1]  # reversal of string to original direction


print(f"Decrypted message: {decrypt(res)}")

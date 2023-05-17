en_key = 1
enk = input("Type something and I will use it to encrypt the next text: \n")
en_key2 = len(enk)


def encrypt(text):
    result = ""
    for char in text:
        if char.isalpha():
            alphabet = 'abcdefghijklmnopqrstuvwxyz' if char.islower() else 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
            shifted = alphabet[(alphabet.index(char) + pow(en_key, en_key2) + (en_key + en_key2)*2) % 26]
            result += shifted
        else:
            result += char
    return result


res = encrypt(input("Enter the text you want to encrypt: \n"))  # 1st encryption
print(f"Encrypted message: {res}")


def decrypt(text):
    result = ""
    for char in text:
        if char.isalpha():
            alphabet = 'abcdefghijklmnopqrstuvwxyz' if char.islower() else 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
            shifted = alphabet[(alphabet.index(char) - pow(en_key, en_key2) - (en_key + en_key2)*2) % 26]
            result += shifted
        else:
            result += char
    return result


print(f"Decrypted message: {decrypt(res)}")

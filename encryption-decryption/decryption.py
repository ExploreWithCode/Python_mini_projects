import keys


def decrypt(text):
    result = ""
    for char in text:
        if char.isalpha():
            alphabet = 'abcdefghijklmnopqrstuvwxyz' if char.islower() else 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
            shifted = alphabet[(alphabet.index(char) - pow(keys.en_key, keys.en_key2) - (keys.en_key + keys.en_key2)*2) % 26]
            result += shifted
        else:
            result += char
    return result


res2 = input("Enter the text you want to decrypt: \n")
print(f"Decrypted message: {decrypt(res2)}")

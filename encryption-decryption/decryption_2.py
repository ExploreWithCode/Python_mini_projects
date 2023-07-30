import keys


def decrypt(text):
    result = ""
    for char in text:
        if char.isalpha():
            if char.islower():
                alphabet = 'abcdefghijklmnopqrstuvwxyz'
                shifted = alphabet[(alphabet.index(char) - pow(keys.en_key, keys.en_key2) - (keys.en_key + keys.en_key2)* 2) % 26]
            else:
                alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
                shifted = alphabet[(alphabet.index(char) - pow(keys.en_key, keys.en_key2) - (keys.en_key + keys.en_key2 + 1)* 2) % 26]
            result += shifted
        else:
            result += char
    return result[::-1]  # reversal of string to original direction


res2 = decrypt(input("Enter the text you want to decrypt: \n"))  # decryption
print(f"Decrypted message: {res2}")

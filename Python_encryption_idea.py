# Create an encryption tool
letters = "abcdefghijklmnopqrstuvwxyz"
en_key = 1
def encrypt(phrase):
    encryption = ""
    for letter in phrase:
        if letter.lower() == letters[0] in letters:
            if letter.isupper():
                encryption = encryption + letters.upper()[0 + en_key]
            else:
                encryption = encryption + letters[0 + en_key]
        elif letter.lower() == letters[1] in letters:
            if letter.isupper():
                encryption = encryption + letters.upper()[1 + en_key]
            else:
                encryption = encryption + letters[1 + en_key]
        else:
            encryption = encryption + letter
    return encryption
  

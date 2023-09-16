from statistics import mode
print("This is a tool that finds the word with the highest value within a given text. Here is how it works: \n"
      "1) A word gets points based on the letters it contains. \"a\"=1, \"b\"=2 etc.\n"
      "2) The numbers are added and show the value of the word.\n"
      "3) In case of a tie, the word with the least characters wins.\n")

txt = input("Give me some text:\n")
txt = txt.lower()
values = []
words = []
for word in txt.split():
      word_value = 0
      for char in word:
            alphabet = "abcdefghijklmnopqrstuvwxyz"
            if char in alphabet:
                  char_value = alphabet.index(char) + 1
                  word_value += char_value
      values.append(word_value)
      if word_value == max(values):
            words.append(word)
print(f"\"{words[-1]}\" was the most valuable word with a value of {max(values)}.")

import numpy
print("This is a tool that finds the word with the highest value within a given text. Here is how it works: \n"
      "1) A word gets points based on the letters it contains. \"a\"=1, \"b\"=2 etc.\n"
      "2) The numbers are added and show the value of the word.\n"
      "3) In case of a tie, the word with the least characters gets printed.\n")
txt = input("Give me some text:\n")
txt = txt.lower()
values, max_words, min_words = [], [], []
for word in txt.split():
      word_value = 0
      for char in word:
            alphabet = "abcdefghijklmnopqrstuvwxyz"
            if char in alphabet:
                  char_value = alphabet.index(char) + 1
                  word_value += char_value
      values.append(word_value)
      if word_value == max(values) and word_value == min(values) and word not in max_words and word not in min_words:
            max_words.append(word)
            min_words.append(word)
      elif word_value == max(values) and word not in max_words:
            max_words.append(word)
      elif word_value == min(values) and word not in min_words:
            min_words.append(word)
print(f"\n\"{max_words[-1]}\" was the most valuable word with a value of {max(values)}.")
print(f"\"{min_words[-1]}\" was the least valuable word with a value of {min(values)}.")
print(f"The average word value is {round(numpy.mean(values))}.")

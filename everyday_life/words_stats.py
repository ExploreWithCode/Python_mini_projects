from statistics import mode
import numpy
txt = input("Give me some text:\n")
print(f"The text contains {len(txt.split())} words.")

number_of_occurrences = 0
length = []
for word in txt.split():
    l_w = len(word)
    if word == mode(txt.split()):
        number_of_occurrences += 1
    length.append(l_w)

print(f"\"{mode(txt.split())}\" was the most common word and was mentioned {number_of_occurrences} times.")
print(f"The average word length was {numpy.mean(length)} characters.")

from statistics import mode
import numpy
txt = input("Give me some text:\n")
print(f"The text contains {len(txt.split())} words.")
number_of_occurrences = 0
length = []
txt = txt.lower()
for word in txt.split():
    l_w = len(word)
    if word == mode(txt.split()):
        number_of_occurrences += 1
    length.append(l_w)
if number_of_occurrences == 1:
    print(f"\"{mode(txt.split())}\" was the most common word and was mentioned {number_of_occurrences} time.")
else:
    print(f"\"{mode(txt.split())}\" was the most common word and was mentioned {number_of_occurrences} times.")
if int(numpy.mean(length)) == 1:
    print(f"The average word length was {int(numpy.mean(length))} character.")
else:
    print(f"The average word length was {int(numpy.mean(length))} characters.")

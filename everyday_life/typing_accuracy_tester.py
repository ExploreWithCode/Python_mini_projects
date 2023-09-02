import random

dictionary = ["man", "library", "see", "interstellar", "odyssey", "journey", "speculation", "rectangular"]
print("Type the word you see.")
points = 0
words_used = 0
while words_used < 5:
    word = random.sample(dictionary, 1)
    print(word)
    inp = input("")
    words_used += 1
    if inp in word:
        points += 1
print(f"Success rate: {round((points / words_used) * 100, 2)}%")
print(f"Total points = {points} / {words_used}")

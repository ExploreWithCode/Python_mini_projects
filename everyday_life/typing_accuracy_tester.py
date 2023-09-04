import random
l2 = ["to", "at", "me", "an", "it", "is", "in", "if", "on", "or", "of", "am", "be", "no", "my", "hi", "oh", "he", "ex"]
l3 = ["off", "man", "men", "for", "boy", "ant", "arm", "art", "bee", "say", "act", "not", "law", "old", "all", "key"]
l4 = ["from", "four", "room", "boom", "zoom", "loot", "bard", "task", "coin", "sign", "mint", "that", "note", "want"]
l5 = ["bloom", "words", "world", "scans", "basic", "merit", "force", "token", "banks", "after", "apply", "quote", "state"]
l6 = ["cancer", "skills", "frozen", "strong", "muscle", "common", "videos", "bureau", "before", "report", "policy"]
l7 = ["scandal", "promise", "falling", "fragile", "magical", "digital", "towards", "warning", "because", "custody"]
l8 = ["illiquid", "provider", "progress", "vampires", "werewolf", "investor", "monetary", "national", "reserve", "project"]
l9 = ["liquidity", "anonymity", "roadmaps", "investors", "framework", "sentiment", "president", "regulation", "statement"]
dictionary = l2 + l3 + l4 + l5 + l6 + l7 + l8 + l9
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

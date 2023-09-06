inp = input("Write some text and I will let you know how many characters it contains:\n")
print(len(inp))
print("Give me a letter or word to know when it first appears in the text")
ind = input("")
# Python starts indexing with 0 instead of 1, so I add 1 to counteract this.
print(f"\"{ind}\" first appears at character {inp.index(ind) + 1}")

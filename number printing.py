print("Which numbers do you want to print?")
print("Give me the starting number: ")
st = int(input())
print("Give me the ending number: ")
en = int(input())
if st > en:
    print("The starting number has to be smaller than the ending number.")
while st <= en:
    print(st, end=" ")
    st += 1

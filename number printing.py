vls = []
brk = ["N", "n"]
print("Which numbers do you want to print?")
while True:
    try:
        print("Give me the starting integer number: ")
        st = int(input())
        print("Give me the ending integer number: ")
        en = int(input())
        if st > en:
            print("The starting number has to be smaller than the ending number.")
        while st <= en:
            print(st, end=" ")
            st += 1
        conf = input("\nPress anything to continue or 'N' quit. ")
        if conf in brk:
            break
    except ValueError:
        print("Invalid input")

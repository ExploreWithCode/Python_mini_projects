brk = ["N", "n"]
print("Which numbers do you want to print?")
while True:
    try:
        print("Give me the starting integer number: ")
        st = input()
        while not st.isnumeric():
            print("Give me an integer!")
            st = input()
        st = int(st)
        print("Give me the ending integer number: ")
        en = input()
        while not en.isnumeric():
            print("Give me an integer!")
            en = input()
        en = int(en)
        while st > en:
            print("The ending number cannot be smaller than the starting number.")
            print(f"Give me an integer smaller than of equal to {st}: ")
            en = input()
            while not en.isnumeric():
                print("Give me an integer!")
                en = input()
            en = int(en)
        en = int(en)
        print("Here is the result:")
        while st <= en:
            print(st, end=" ")
            st += 1
        conf = input("\nPress anything to continue or 'N' to quit. ")
        if conf in brk:
            break
    except ValueError:
        print("Invalid input!")

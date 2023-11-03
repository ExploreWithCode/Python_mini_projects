brk = ["Q", "q"]
print("Which numbers do you want to print?")
while True:
    try:
        st = input("Give me the starting integer number: ")
        while not st.isnumeric():
            st = input("Give me an integer: ")
        st = int(st)
        en = input("Give me the ending integer number: ")
        while not en.isnumeric():
            en = input("Give me an integer: ")
        en = int(en)
        while st > en:
            print("The ending number cannot be smaller than the starting number!")
            en = input(f"Give me an integer smaller than or equal to {st}: ")
            while not en.isnumeric():
                en = input("Give me an integer: ")
            en = int(en)
        en = int(en)
        print("\nHere is the result:")
        while st <= en:
            print(st, end=" ")
            st += 1
        conf = input("\nPress either 'Q' or 'q' to quit or anything else to continue. ")
        if conf in brk:
            break
    except ValueError:
        print("Invalid input!")

accepted_passwords = ["cage", "dragon", "key"]
message = ["Veritas", "means \"truth\"."]
current_value = 0
minimum_acceptable = 2
guess = guess2 = ""
guess_count = guess_count2 = 0
guess_limit = 3
out_of_guesses = out_of_guesses2 = False
left = left2 = guess_limit

while guess not in accepted_passwords and not out_of_guesses:
    if guess_count < guess_limit:
        print(f"You have {left} guesses!")
        left -= 1
        guess = input("Give me a password: ")
        guess_count += 1
    else:
        out_of_guesses = True

if out_of_guesses:
    print("Out of guesses!")
else:
    print("Correct!")
    current_value += 1
    while guess2 not in accepted_passwords and not out_of_guesses2:
        if guess_count2 < guess_limit:
            print(f"You have {left2} guesses!")
            left2 -= 1
            guess2 = input("Give me a second (and different) password: ")
            guess_count2 += 1
        else:
            out_of_guesses2 = True
    if out_of_guesses2:
        print("Out of guesses for the second password!")
    elif guess2 == guess:
        print(f"You have 1 guess, because you tried to use the same password!")
        guess2 = input("Give me a second (and different) password: ")
        if guess2 in accepted_passwords and guess2 != guess:
            print("Correct second password!")
            current_value += 1
        else:
            out_of_guesses2 = True
    else:
        print("Correct second password!")
        current_value += 1
    
if current_value == minimum_acceptable:
    print(f"\n{message[0]} {message[1]}")
else:
    print("\nThe process failed!")

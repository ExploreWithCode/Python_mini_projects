accepted_1 = "cage"
accepted_2 = "dragon"
accepted_3 = "key"
message_pt1 = "Veritas"
message_pt2 = "means \"truth\"."
current_value = 0
minimum_acceptable = 2
guess = ""
guess2 = ""
guess_count = 0
guess_count2 = 0
guess_count_same = 0
guess_limit = 3
out_of_guesses = False
out_of_guesses2 = False
left = guess_limit
left2 = guess_limit

while guess != accepted_1 and guess != accepted_2 and guess != accepted_3 and not(out_of_guesses):
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

while guess2 != accepted_1 and guess2 != accepted_2 and guess2 != accepted_3 and not(out_of_guesses2):
    if guess_count2 < guess_limit:
        print(f"You have {left2} guesses!")
        left2 -= 1
        guess2 = input("Give me a second (and different) password: ")
        guess_count2 += 1
    else:
        out_of_guesses2 = True
        
if out_of_guesses2:
    print("Out of guesses!")
elif guess2 == guess:
    print(f"You have 1 guess, because you tried to use the same password!")
    guess2 = input("Give me a second (and different) password: ")
    if guess2 == accepted_1 or guess2 == accepted_2 or guess2 == accepted_3 and guess2 != guess:
        print("Correct second password!")
        current_value += 1
    else:
        out_of_guesses2 = True
else:
    print("Correct second password!")
    current_value += 1
    
if current_value == minimum_acceptable:
    print(f"\n{message_pt1} {message_pt2}")
else:
    print("\nThe process failed!")

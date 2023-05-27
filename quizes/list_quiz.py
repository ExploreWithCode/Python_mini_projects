points = 0
print("Find an item in a given list. Use uppercase and lowercase appropriately.")
scand_cntrs = ["Norway", "Finland", "Sweden"]
inp1 = input("1) Scandinavian countries: ")
if inp1 in scand_cntrs:
    points += 1
    print("Got it!")
else:
    print("Not in the list")
scand_cntrs = ["Vatican City", "Monaco", "San Marino", "Liechtenstein", "Malta", "Andorra"]
inp2 = input("2) European microstates: ")
if inp2 in scand_cntrs:
    points += 1
    print("Got it!")
else:
    print("Not in the list")
questions = (inp1, inp2)
q = len(questions)
print(f"Sucess rate: {round((points / q) * 100, 2)}%")
print(f"Total points = {points}")

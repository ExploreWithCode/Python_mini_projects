points = 0
accepted = "ABCDabcd"
print("This is a multiple choice quiz. Answer correctly to get points.")
print("1) Which of the following is NOT a fully supported Python programming paradigm?")
inp1 = input("A: object-oriented | B: structured | C: logic | D: all of the above\n")
if inp1 not in accepted:
    print("Not an accepted answer!")
elif inp1 == "C" or inp1 == "c":
    points += 1
    print("Correct!")
else:
    print("Wrong answer!")
print("2) Name the collection of principles that influence the design of Python:")
inp2 = input("A: Python Guiding Principles | B: Zen of Python | C: Principles For The Snake | D: The Python's Principles\n")
if inp2 not in accepted:
    print("Not an accepted answer!")   
elif inp2 == "B" or inp2 == "b":
    points += 1
    print("Correct!")
else:
    print("Wrong answer!")
print("3) Python was first released in:")
inp3 = input("A: 1980 | B: 1991 | C: 2000 | D: 2008\n")
if inp3 not in accepted:
    print("Not an accepted answer!")    
elif inp3 == "B" or inp3 == "b":
    points += 1
    print("Correct!")
else:
    print("Wrong answer!")
questions = (inp1, inp2, inp3)
q = len(questions)
print(f"Success rate: {round((points/q) * 100, 2)}%")
print(f"Total points = {points}/{q}")

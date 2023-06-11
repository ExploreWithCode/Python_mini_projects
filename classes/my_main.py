from classes import Character

character1 = Character("Sam", "Business", 31, False)
character2 = Character("Rita", "Art", 25, True)
character3 = Character("Martin", "Tourism", 80, False)
character4 = Character("Nina", "Music", 58, True)
character5 = Character("David", "Finance", 40, True)
character6 = Character("Jax", "Cinematography", 21, True)

chars = (1, 2, 3, 4, 5, 6)


def funk(text):
    st_num = "character "
    st_num += text
    return st_num


inpu = (input("Insert a number here:\n"))
inp = funk(inpu)
print(inp, end=" ")
if inp == "character 1":
    print(f"\nName: {character1.name}, Interest: {character1.interest}, Age: {character1.age}, Alive: {character1.is_alive}")
elif inp == "character 2":
    print(f"\nName: {character2.name}, Interest: {character2.interest}, Age: {character2.age}, Alive: {character2.is_alive}")
elif inp == "character 3":
    print(f"\nName: {character3.name}, Interest: {character3.interest}, Age: {character3.age}, Alive: {character3.is_alive}")
elif inp == "character 4":
    print(f"\nName: {character4.name}, Interest: {character4.interest}, Age: {character4.age}, Alive: {character4.is_alive}")
elif inp == "character 5":
    print(f"\nName: {character5.name}, Interest: {character5.interest}, Age: {character5.age}, Alive: {character5.is_alive}")
elif inp == "character 6":
    print(f"\nName: {character6.name}, Interest: {character6.interest}, Age: {character6.age}, Alive: {character6.is_alive}")
elif not inpu.isnumeric():
    print("I want a number!")
elif inpu not in chars:
    print("does not exist!")
else:
    print("Error!")

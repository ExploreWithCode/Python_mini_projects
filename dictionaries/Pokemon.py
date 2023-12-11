inp = input("Give me a pokemon's name or Pokedex number and you will receive the other plus its type(s):\n")
inp = inp.capitalize()
pokemon = {
    1: ["Bulbasaur", "Grass/Poison"],
    2: ["Ivysaur", "Grass/Poison"],
    3: ["Venusaur", "Grass/Poison"],
    4: ["Charmander", "Fire"],
    5: ["Charmeleon", "Fire"],
    6: ["Charizard", "Fire/Flying"],
    7: ["Squirtle", "Water"],
    8: ["Wartortle", "Water"],
    9: ["Blastoise", "Water"],
    10: ["Caterpie", "Bug"],
    11: ["Metapod", "Bug"],
    12: ["Butterfree", "Bug/Flying"]
}
pokeys = list(pokemon.keys())
trick = 0
if inp in pokemon:
    print(f"Name: {pokemon[inp][0]} | Pokedex number: {inp} | Type: {pokemon[inp][1]}")
    trick = 1
else:
    for index, i in enumerate(pokemon):
        if inp in pokemon[i][0]:
            print(f"Name: {pokemon[i][0]} | Pokedex number: {pokeys[index]} | Type: {pokemon[i][1]}")
            trick = 1
            break

if trick == 0:
    print("Your input has no match in the database!\n"
          "Make sure you insert no spaces or other unnecessary characters.\n"
          "Also type an existing name, symbol or atomic number.")

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
    12: ["Butterfree", "Bug/Flying"],
    13: ["Weedle", "Bug/Poison"],
    14: ["Kakuna", "Bug/Poison"],
    15: ["Beedrill", "Bug/Poison"],
    16: ["Pidgey", "Normal/Flying"],
    17: ["Pidgeotto", "Normal/Flying"],
    18: ["Pidgeot", "Normal/Flying"],
    19: ["Rattata", "Normal"],
    20: ["Raticate", "Normal"],
    21: ["Spearow", "Normal/Flying"],
    22: ["Fearow", "Normal/Flying"],
    23: ["Ekans", "Poison"],
    24: ["Arbok", "Poison"],
    25: ["Pikachu", "Electric"],
    26: ["Raichu", "Electric"],
    27: ["Sandshrew", "Ground"],
    28: ["Sandslash", "Ground"],
    29: ["Nidoran♀", "Poison"],
    30: ["Nidorina", "Poison"],
    31: ["Nidoqueen", "Poison/Ground"],
    32: ["Nidoran♂", "Poison"],
    33: ["Nidorino", "Poison"],
    34: ["Nidoking", "Poison/Ground"],
    35: ["Clefairy", "Fairy"],
    36: ["Clefable", "Fairy"],
    37: ["Vulpix", "Fire"],
    38: ["Ninetales", "Fire"],
    39: ["Jigglypuff", "Normal/Fairy"],
    40: ["Wigglytuff", "Normal/Fairy"],
    41: ["Zubat", "Poison/Flying"],
    42: ["Golbat", "Poison/Flying"],
    43: ["Oddish", "Grass/Poison"],
    44: ["Gloom", "Grass/Poison"],
    45: ["Vileplume", "Grass/Poison"],
    46: ["Paras", "Bug/Grass"],
    47: ["Parasect", "Bug/Grass"],
    48: ["Venonat", "Bug/Poison"],
    49: ["Venomoth", "Bug/Poison"],
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

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
    50: ["Diglett", "Ground"],
    51: ["Dugtrio", "Ground"],
    52: ["Meowth", "Normal"],
    53: ["Persian", "Normal"],
    54: ["Psyduck", "Water"],
    55: ["Golduck", "Water"],
    56: ["Mankey", "Fighting"],
    57: ["Primeape", "Fighting"],
    58: ["Growlithe", "Fire"],
    59: ["Arcanine", "Fire"],
    60: ["Poliwag", "Water"],
    61: ["Poliwhirl", "Water"],
    62: ["Poliwrath", "Water/Fighting"],
    63: ["Abra", "Psychic"],
    64: ["Kadabra", "Psychic"],
    65: ["Alakazam", "Psychic"],
    66: ["Machop", "Fighting"],
    67: ["Machoke", "Fighting"],
    68: ["Machamp", "Fighting"],
    69: ["Bellsprout", "Grass/Poison"],
    70: ["Weepinbell", "Grass/Poison"],
    71: ["Victreebel", "Grass/Poison"],
    72: ["Tentacool", "Water/Poison"],
    73: ["Tentacruel", "Water/Poison"],
    74: ["Geodude", "Rock/Ground"],
    75: ["Graveler", "Rock/Ground"],
    76: ["Golem", "Rock/Ground"],
    77: ["Ponyta", "Fire"],
    78: ["Rapidash", "Fire"],
    79: ["Slowpoke", "Psychic"],
    80: ["Slowbro", "Psychic"],
    81: ["Magnemite", "Electric"],
    82: ["Magneton", "Electric"],
    83: ["Farfetch'd", "Normal"],
    84: ["Doduo", "Normal"],
    85: ["Dodrio", "Normal"],
    86: ["Seel", "Water"],
    87: ["Dewgong", "Water"],
    88: ["Grimer", "Poison"],
    89: ["Muk", "Poison"],
    90: ["Shellder", "Water"],
    91: ["Cloyster", "Water/Ice"],
    92: ["Gastly", "Ghost/Poison"],
    93: ["Haunter", "Ghost/Poison"],
    94: ["Gengar", "Ghost/Poison"],
    95: ["Onix", "Rock/Ground"],
    96: ["Drowzee", "Psychic"],
    97: ["Hypno", "Psychic"],
    98: ["Krabby", "Water"],
    99: ["Kingler", "Water"],
    100: ["Voltorb", "Electric"],
    101: ["Electrode", "Electric"],
    102: ["Exeggcute", "Grass/Psychic"],
    103: ["Exeggutor", "Grass/Psychic"],
    104: ["Cubone", "Ground"],
    105: ["Marowak", "Ground"],
    106: ["Hitmonlee", "Fighting"],
    107: ["Hitmonchan", "Fighting"],
    108: ["Lickitung", "Normal"],
    109: ["Koffing", "Poison"],
    110: ["Weezing", "Poison"],
    111: ["Rhyhorn", "Ground/Rock"],
    112: ["Rhydon", "Ground/Rock"],
    113: ["Chansey", "Normal"],
    114: ["Tangela", "Grass"],
    115: ["Kangaskhan", "Normal"],
    116: ["Horsea", "Water"],
    117: ["Seadra", "Water"],
    118: ["Goldeen", "Water"],
    119: ["Seaking", "Water"],
    120: ["Staryu", "Water"],
    121: ["Starmie", "Water/Psychic"],
    122: ["Mr. Mime", "Psychic/Fairy"],
    123: ["Scyther", "Bug/Flying"],
    124: ["Jynx", "Ice/Psychic"],
    125: ["Electabuzz", "Electric"],
    126: ["Magmar", "Fire"],
    127: ["Pinsir", "Bug"],
    128: ["Tauros", "Normal"],
    129: ["Magikarp", "Water"],
    130: ["Gyarados", "Water/Flying"],
    131: ["Lapras", "Water"],
    132: ["Ditto", "Psychic"],
    133: ["Eevee", "Normal"],
    134: ["Vaporeon", "Water"],
    135: ["Jolteon", "Electric"],
    136: ["Flareon", "Fire"],
    137: ["Porygon", "Electric"],
    138: ["Omanyte", "Water"],
    139: ["Omastar", "Water"],
    140: ["Kabuto", "Water"],
    141: ["Kabutops", "Water"],
    142: ["Aerodactyl", "Rock"],
    143: ["Snorlax", "Normal"],
    144: ["Articuno", "Ice"],
    145: ["Zapdos", "Electric"],
    146: ["Moltres", "Fire"],
    147: ["Dratini", "Dragon"],
    148: ["Dragonair", "Dragon"],
    149: ["Dragonite", "Dragon"],
    150: ["Mewtwo", "Psychic"],
    151: ["Mew", "Psychic"],    # Gen 1 ends here
    152: ["Chikorita", "Grass"],
    153: ["Bayleef", "Grass"],
    154: ["Meganium", "Grass"],
    155: ["Cyndaquil", "Fire"],
    156: ["Quilava", "Fire"],
    157: ["Typhlosion", "Fire"],
    158: ["Totodile", "Water"],
    159: ["Croconaw", "Water"],
    160: ["Feraligatr", "Water"],
    161: ["Sentret", "Normal"],
    162: ["Furret", "Normal"],
    163: ["Hoothoot", "Normal/Flying"],
    164: ["Noctowl", "Normal/Flying"],
    165: ["Ledyba", "Bug/Flying"],
    166: ["Ledian", "Bug/Flying"],
    167: ["Spinarak", "Bug/Poison"],
    168: ["Ariados", "Bug/Poison"],
    169: ["Crobat", "Poison/Flying"],
    170: ["Chinchou", "Water/Electric"],
    171: ["Lanturn", "Water/Electric"],
    172: ["Pichu", "Electric"],
    173: ["Cleffa", "Fairy"],
    174: ["Igglybuff", "Normal/Fairy"],
    175: ["Togepi", "Fairy"],
    176: ["Togetic", "Fairy/Flying"],
    177: ["Natu", "Psychic/Flying"],
    178: ["Xatu", "Psychic/Flying"],
    179: ["Mareep", "Electric"],
    180: ["Flaaffy", "Electric"],
    181: ["Ampharos", "Electric"],
    182: ["Bellossom", "Grass"],
    183: ["Marill", "Water/Fairy"],
    184: ["Azumarill", "Water/Fairy"],
    185: ["Sudowoodo", "Rock"],
    186: ["Politoed", "Water"],
    187: ["Hoppip", "Grass/Flying"],
    188: ["Skiploom", "Grass/Flying"],
    189: ["Jumpluff", "Grass/Flying"],
    190: ["Aipom", "Normal"],
    191: ["Sunkern", "Grass"],
    192: ["Sunflora", "Grass"],
    193: ["Yanma", "Bug/Flying"],
    194: ["Wooper", "Water/Ground"],
    195: ["Quagsire", "Water/Ground"],
    196: ["Espeon", "Psychic"],
    197: ["Umbreon", "Dark"],
    198: ["Murkrow", "Dark/Flying"],
    199: ["Slowking", "Water/Psychic"],
    200: ["Misdreavus", "Ghost"],
    201: ["Unown", "Psychic"],
    202: ["Wobbuffet", "Psychic"],
    203: ["Girafarig", "Normal/Psychic"],
    204: ["Pineco", "Bug"],
    205: ["Forretress", "Bug/Steel"],
    206: ["Dunsparce", "Normal"],
    207: ["Gligar", "Ground/Flying"],
    208: ["Steelix", "Steel/Ground"],
    209: ["Snubbull", "Fairy"],
    210: ["Granbull", "Fairy"],
    211: ["Qwilfish", "Water/Poison"],
    212: ["Scizor", "Bug/Steel"],
    213: ["Shuckle", "Bug/Rock"],
    214: ["Heracross", "Bug/Fighting"],
    215: ["Sneasel", "Dark/Ice"],
    216: ["Teddiursa", "Normal"],
    217: ["Ursaring", "Normal"],
    218: ["Slugma", "Fire"],
    219: ["Magcargo", "Fire/Rock"],
    220: ["Swinub", "Ice/Ground"],
    221: ["Piloswine", "Ice/Ground"],
    222: ["Corsola", "Water/Rock"],
    223: ["Remoraid", "Water"],
    224: ["Octillery", "Water"],
    225: ["Delibird", "Ice/Flying"],
    226: ["Mantine", "Water/Flying"],
    227: ["Skarmory", "Steel/Flying"],
    228: ["Houndour", "Dark/Fire"],
    229: ["Houndoom", "Dark/Fire"],
    230: ["Kingdra", "Water/Dragon"],
    231: ["Phanpy", "Ground"],
    232: ["Donphan", "Ground"],
    233: ["Porygon2", "Electric"],
    234: ["Stantler", "Ground"],
    235: ["Smeargle", "Normal"],
    236: ["Tyrogue", "Fighting"],
    237: ["Hitmontop", "Fighting"],
    238: ["Smoochum", "Ice/Psychic"],
    239: ["Elekid", "Electric"],
    240: ["Magby", "Fire"],
    241: ["Miltank", "Normal"],
    242: ["Blissey", "Normal"],
    243: ["Raikou", "Electric"],
    244: ["Entei", "Fire"],
    245: ["Suicune", "Water"],
    246: ["Larvitar", "Rock/Ground"],
    247: ["Pupitar", "Rock/Ground"],
    248: ["Tyranitar", "Rock/Dark"],
    249: ["Lugia", "Psychic/Flying"],
    250: ["Ho-Oh", "Fire/Flying"],
    251: ["Celebi", "Psychic/Grass"],    # Gen 2 ends here
    351: ["Castform", "Normal"]
}
pokeys = list(pokemon.keys())

Gen1_keys = pokeys[1-1:151+1]  # 1-151
Gen2_keys = pokeys[152-1:251+1]  # 152-251
'''
Gen3_keys = pokeys[252-1:386-1]
Gen4_keys = pokeys[387-1:493-1]
Gen5_keys = pokeys[494-1:649-1]
Gen6_keys = pokeys[650-1:721-1]
Gen7_keys = pokeys[722-1:809-1]
Gen8_keys = pokeys[810-1:905-1]
Gen9_keys = pokeys[906-1:1025-1]
'''

Alolan_Form = {}
Galarian_Form = {}
Hisuian_Form = {}
Paldean_Form = {}
Multiform = {    # Some don't change type between forms/modes
    "Castform": [351,
                 {"Normal Form": "Normal",
                  "Sunny Form": "Fire",
                  "Rainy Form": "Water ",
                  "Snowy Form": "Ice"}]
}
trick = 0
for index, i in enumerate(pokemon):
    if inp == pokemon[i][0]:    # -WHERE
        # names
        if pokeys[1-1] < pokeys[index] <= pokeys[151-1]:    # --Generations
            print("Generation I")
        elif pokeys[152-1] <= pokeys[index] <= pokeys[251-1]:
            print("Generation II")
        print(f"Name: {pokemon[i][0]} | Pokedex number: {pokeys[index]} | Type: {pokemon[i][1]}")
        if inp in Multiform:    # --Forms
            print(Multiform[inp][1])
        trick = 1
        break
    elif inp == str(i):    # -WHERE
        # numbers
        try:
            if pokeys[int(inp) - 1] in Gen1_keys:    # --Generations
                print("Generation I")
            elif pokeys[int(inp) - 1] in Gen2_keys:
                print("Generation II")
        except IndexError:
            print("The pokemon has not yet been assigned to a generation.")
        print(f"Name: {pokemon[i][0]} | Pokedex number: {pokeys[index]} | Type: {pokemon[i][1]}")
        for mi in Multiform:    # --Forms
            if int(inp) == Multiform[mi][0]:
                print(Multiform[mi][1])
        trick = 1
        break
    elif inp in pokemon[i][1]:
        print(f"{i}: {pokemon[i]}")
        trick = 1

if trick == 0:
    print("Your input has no match in the database!\n"
          "Make sure you insert no spaces or other unnecessary characters.\n"
          "Also type an existing name or Pokedex number.")

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
    79: ["Slowpoke", "Water/Psychic"],
    80: ["Slowbro", "Water/Psychic"],
    81: ["Magnemite", "Electric/Steel"],
    82: ["Magneton", "Electric/Steel"],
    83: ["Farfetch'd", "Normal/Flying"],
    84: ["Doduo", "Normal/Flying"],
    85: ["Dodrio", "Normal/Flying"],
    86: ["Seel", "Water"],
    87: ["Dewgong", "Water/Ice"],
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
    131: ["Lapras", "Water/Ice"],
    132: ["Ditto", "Normal"],
    133: ["Eevee", "Normal"],
    134: ["Vaporeon", "Water"],
    135: ["Jolteon", "Electric"],
    136: ["Flareon", "Fire"],
    137: ["Porygon", "Normal"],
    138: ["Omanyte", "Rock/Water"],
    139: ["Omastar", "Rock/Water"],
    140: ["Kabuto", "Rock/Water"],
    141: ["Kabutops", "Rock/Water"],
    142: ["Aerodactyl", "Rock/Flying"],
    143: ["Snorlax", "Normal"],
    144: ["Articuno", "Ice/Flying"],
    145: ["Zapdos", "Electric/Flying"],
    146: ["Moltres", "Fire/Flying"],
    147: ["Dratini", "Dragon"],
    148: ["Dragonair", "Dragon"],
    149: ["Dragonite", "Dragon/Flying"],
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
    233: ["Porygon2", "Normal"],
    234: ["Stantler", "Normal"],
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
    252: ["Treecko", "Grass"],
    253: ["Grovyle", "Grass"],
    254: ["Sceptile", "Grass"],
    255: ["Torchic", "Fire"],
    256: ["Combusken", "Fire/Fighting"],
    257: ["Blaziken", "Fire/Fighting"],
    258: ["Mudkip", "Water"],
    259: ["Marshtomp", "Water/Ground"],
    260: ["Swampert", "Water/Ground"],
    261: ["Poochyena", "Dark"],
    262: ["Mightyena", "Dark"],
    263: ["Zigzagoon", "Normal"],
    264: ["Linoone", "Normal"],
    265: ["Wurmple", "Bug"],
    266: ["Silcoon", "Bug"],
    267: ["Beautifly", "Bug/Flying"],
    268: ["Cascoon", "Bug"],
    269: ["Dustox", "Bug/Poison"],
    270: ["Lotad", "Water/Grass"],
    271: ["Lombre", "Water/Grass"],
    272: ["Ludicolo", "Water/Grass"],
    273: ["Seedot", "Grass"],
    274: ["Nuzleaf", "Grass/Dark"],
    275: ["Shiftry", "Grass/Dark"],
    276: ["Taillow", "Normal/Flying"],
    277: ["Swellow", "Normal/Flying"],
    278: ["Wingull", "Water/Flying"],
    279: ["Pelipper", "Water/Flying"],
    280: ["Ralts", "Psychic/Fairy"],
    281: ["Kirlia", "Psychic/Fairy"],
    282: ["Gardevoir", "Psychic/Fairy"],
    283: ["Surskit", "Bug/Water"],
    284: ["Masquerain", "Bug/Flying"],
    285: ["Shroomish", "Grass"],
    286: ["Breloom", "Grass/Fighting"],
    287: ["Slakoth", "Normal"],
    288: ["Vigoroth", "Normal"],
    289: ["Slaking", "Normal"],
    290: ["Nincada", "Bug/Ground"],
    291: ["Ninjask", "Bug/Flying"],
    292: ["Shedinja", "Bug/Ghost"],
    293: ["Whismur", "Normal"],
    294: ["Loudred", "Normal"],
    295: ["Exploud", "Normal"],
    296: ["Makuhita", "Fighting"],
    297: ["Hariyama", "Fighting"],
    298: ["Azurill", "Normal/Fairy"],
    299: ["Nosepass", "Rock"],
    300: ["Skitty", "Normal"],
    301: ["Delcatty", "Normal"],
    302: ["Sableye", "Dark/Ghost"],
    303: ["Mawile", "Steel/Fairy"],
    304: ["Aron", "Steel/Rock"],
    305: ["Lairon", "Steel/Rock"],
    306: ["Aggron", "Steel/Rock"],
    307: ["Meditite", "Fighting/Psychic"],
    308: ["Medicham", "Fighting/Psychic"],
    309: ["Electrike", "Electric"],
    310: ["Manectric", "Electric"],
    311: ["Plusle", "Electric"],
    312: ["Minun", "Electric"],
    313: ["Volbeat", "Bug"],
    314: ["Illumise", "Bug"],
    315: ["Roselia", "Grass/Poison"],
    316: ["Gulpin", "Poison"],
    317: ["Swalot", "Poison"],
    318: ["Carvanha", "Water/Dark"],
    319: ["Sharpedo", "Water/Dark"],
    320: ["Wailmer", "Water"],
    321: ["Wailord", "Water"],
    322: ["Numel", "Fire/Ground"],
    323: ["Camerupt", "Fire/Ground"],
    324: ["Torkoal", "Fire"],
    325: ["Spoink", "Psychic"],
    326: ["Grumpig", "Psychic"],
    327: ["Spinda", "Normal"],
    328: ["Trapinch", "Ground"],
    329: ["Vibrava", "Ground/Dragon"],
    330: ["Flygon", "Ground/Dragon"],
    331: ["Cacnea", "Grass"],
    332: ["Cacturne", "Grass/Dark"],
    333: ["Swablu", "Normal/Flying"],
    334: ["Altaria", "Dragon/Flying"],
    335: ["Zangoose", "Normal"],
    336: ["Seviper", "Poison"],
    337: ["Lunatone", "Rock/Psychic"],
    338: ["Solrock", "Rock/Psychic"],
    339: ["Barboach", "Water/Ground"],
    340: ["Whiscash", "Water/Ground"],
    341: ["Corphish", "Water"],
    342: ["Crawdaunt", "Water/Dark"],
    343: ["Baltoy", "Ground/Psychic"],
    344: ["Claydol", "Ground/Psychic"],
    345: ["Lileep", "Rock/Grass"],
    346: ["Cradily", "Rock/Grass"],
    347: ["Anorith", "Rock/Bug"],
    348: ["Armaldo", "Rock/Bug"],
    349: ["Feebas", "Water"],
    350: ["Milotic", "Water"],
    351: ["Castform", "Normal"],
    352: ["Kecleon", "Normal"],
    353: ["Shuppet", "Ghost"],
    354: ["Banette", "Ghost"],
    355: ["Duskull", "Ghost"],
    356: ["Dusclops", "Ghost"],
    357: ["Tropius", "Grass/Flying"],
    358: ["Chimecho", "Psychic"],
    359: ["Absol", "Dark"],
    360: ["Wynaut", "Psychic"],
    361: ["Snorunt", "Ice"],
    362: ["Glalie", "Ice"],
    363: ["Spheal", "Ice/Water"],
    364: ["Sealeo", "Ice/Water"],
    365: ["Walrein", "Ice/Water"],
    366: ["Clamperl", "Water"],
    367: ["Huntail", "Water"],
    368: ["Gorebyss", "Water"],
    369: ["Relicanth", "Water/Rock"],
    370: ["Luvdisc", "Water"],
    371: ["Bagon", "Dragon"],
    372: ["Shelgon", "Dragon"],
    373: ["Salamence", "Dragon/Flying"],
    374: ["Beldum", "Steel/Psychic"],
    375: ["Metang", "Steel/Psychic"],
    376: ["Metagross", "Steel/Psychic"],
    377: ["Regirock", "Rock"],
    378: ["Regice", "Ice"],
    379: ["Registeel", "Steel"],
    380: ["Latias", "Dragon/Psychic"],
    381: ["Latios", "Dragon/Psychic"],
    382: ["Kyogre", "Water"],
    383: ["Groudon", "Ground"],
    384: ["Rayquaza", "Dragon/Flying"],
    385: ["Jirachi", "Steel/Psychic"],
    386: ["Deoxys", "Psychic"],    # Gen 3 ends here
    387: ["Turtwig", "Grass"],
    388: ["Grotle", "Grass"],
    389: ["Torterra", "Grass/Ground"],
    390: ["Chimchar", "Fire"],
    391: ["Monferno", "Fire/Fighting"],
    392: ["Infernape", "Fire/Fighting"],
    393: ["Piplup", "Water"],
    394: ["Prinplup", "Water"],
    395: ["Empoleon", "Water/Steel"],
    396: ["Starly", "Normal/Flying"],
    397: ["Staravia", "Normal/Flying"],
    398: ["Staraptor", "Normal/Flying"],
    399: ["Bidoof", "Normal"],
    400: ["Bibarel", "Normal/Water"],
    401: ["Kricketot", "Bug"],
    402: ["Kricketune", "Bug"],
    403: ["Shinx", "Electric"],
    404: ["Luxio", "Electric"],
    405: ["Luxray", "Electric"],
    406: ["Budew", "Grass/Poison"],
    407: ["Roserade", "Grass/Poison"],
    408: ["Cranidos", "Rock"],
    409: ["Rampardos", "Rock"],
    410: ["Shieldon", "Rock/Steel"],
    411: ["Bastiodon", "Rock/Steel"],
    412: ["Burmy", "Bug"],
    413: ["Wormadam", "Bug/Grass"],
    414: ["Mothim", "Bug/Flying"],
    415: ["Combee", "Bug/Flying"],
    416: ["Vespiquen", "Bug/Flying"],
    417: ["Pachirisu", "Electric"],
    418: ["Buizel", "Water"],
    419: ["Floatzel", "Water"],
    420: ["Cherubi", "Grass"],
    421: ["Cherrim", "Grass"],
    422: ["Shellos", "Water"],
    423: ["Gastrodon", "Water/Ground"],
    424: ["Ambipom", "Normal"],
    425: ["Drifloon", "Ghost/Flying"],
    426: ["Drifblim", "Ghost/Flying"],
    427: ["Buneary", "Normal"],
    428: ["Lopunny", "Normal"],
    429: ["Mismagius", "Ghost"],
    430: ["Honchkrow", "Dark/Flying"],
    431: ["Glameow", "Normal"],
    432: ["Purugly", "Normal"],
    433: ["Chingling", "Psychic"],
    434: ["Stunky", "Poison/Dark"],
    435: ["Skuntank", "Poison/Dark"],
    436: ["Bronzor", "Steel/Psychic"],
    437: ["Bronzong", "Steel/Psychic"],
    438: ["Bonsly", "Rock"],
    439: ["Mime Jr.", "Psychic/Fairy"],
    440: ["Happiny", "Normal"],
    441: ["Chatot", "Normal/Flying"],
    442: ["Spiritomb", "Ghost/Dark"],
    443: ["Gible", "Dragon/Ground"],
    444: ["Gabite", "Dragon/Ground"],
    445: ["Garchomp", "Dragon/Ground"],
    446: ["Munchlax", "Normal"],
    447: ["Riolu", "Fighting"],
    448: ["Lucario", "Fighting/Steel"],
    449: ["Hippopotas", "Ground"],
    450: ["Hippowdon", "Ground"],
    451: ["Skorupi", "Poison/Bug"],
    452: ["Drapion", "Poison/Dark"],
    453: ["Croagunk", "Poison/Fighting"],
    454: ["Toxicroak", "Poison/Fighting"],
    455: ["Carnivine", "Grass"],
    456: ["Finneon", "Water"],
    457: ["Lumineon", "Water"],
    458: ["Mantyke", "Water/Flying"],
    459: ["Snover", "Grass/Ice"],
    460: ["Abomasnow", "Grass/Ice"],
    461: ["Weavile", "Dark/Ice"],
    462: ["Magnezone", "Electric/Steel"],
    463: ["Lickilicky", "Normal"],
    464: ["Rhyperior", "Ground/Rock"],
    465: ["Tangrowth", "Grass"],
    466: ["Electivire", "Electric"],
    467: ["Marmortar", "Fire"],
    468: ["Togekiss", "Fairy/Flying"],
    469: ["Yanmega", "Bug/Flying"],
    470: ["Leafeon", "Grass"],
    471: ["Glaceon", "Ice"],
    472: ["Gliscor", "Ground/Flying"],
    473: ["Mamoswine", "Ice/Ground"],
    474: ["Porygon-Z", "Normal"],
    475: ["Gallade", "Psychic/Fighting"],
    476: ["Probopass", "Rock/Steel"],
    477: ["Dusknoir", "Ghost"],
    478: ["Froslass", "Ice/Ghost"],
    479: ["Rotom", "Electric/Ghost"],
    480: ["Uxie", "Psychic"],
    481: ["Mesprit", "Psychic"],
    482: ["Azelf", "Psychic"],
    483: ["Dialga", "Steel/Dragon"],
    484: ["Palkia", "Water/Dragon"],
    485: ["Heatran", "Fire/Steel"],
    486: ["Regigigas", "Normal"],
    487: ["Giratina", "Ghost/Dragon"],
    488: ["Cresselia", "Psychic"],
    489: ["Phione", "Water"],
    490: ["Manaphy", "Water"],
    491: ["Darkrai", "Dark"],
    492: ["Shaymin", "Grass"],
    493: ["Arceus", "Normal"],    # Gen 4 ends here
    494: ["Victini", "Psychic/Fire"],
    495: ["Snivy", "Grass"],
    496: ["Servine", "Grass"],
    497: ["Serperior", "Grass"],
    498: ["Tepig", "Fire"],
    499: ["Pignite", "Fire/Fighting"],
    500: ["Emboar", "Fire/Fighting"],
    501: ["Oshawott", "Water"],
    502: ["Dewott", "Water"],
    503: ["Samurott", "Water"],
    504: ["Patrat", "Normal"],
    505: ["Watchog", "Normal"],
    506: ["Lillipup", "Normal"],
    507: ["Herdier", "Normal"],
    508: ["Stoutland", "Normal"],
    509: ["Purrloin", "Dark"],
    510: ["Liepard", "Dark"],
    511: ["Pansage", "Grass"],
    512: ["Simisage", "Grass"],
    513: ["Pansear", "Fire"],
    514: ["Simisear", "Fire"],
    515: ["Panpour", "Water"],
    516: ["Simipour", "Water"],
    517: ["Munna", "Psychic"],
    518: ["Musharna", "Psychic"],
    519: ["Pidove", "Normal/Flying"],
    520: ["Tranquill", "Normal/Flying"],
    521: ["Unfezant", "Normal/Flying"],
    522: ["Blitzle", "Electric"],
    523: ["Zebstrika", "Electric"],
    524: ["Roggenrola", "Rock"],
    525: ["Boldore", "Rock"],
    526: ["Gigalith", "Rock"],
    527: ["Woobat", "Psychic/Flying"],
    528: ["Swoobat", "Psychic/Flying"],
    529: ["Drilbur", "Ground"],
    530: ["Excadrill", "Ground/Steel"],
    531: ["Audino", "Normal"],
    532: ["Timburr", "Fighting"],
    533: ["Gurdurr", "Fighting"],
    534: ["Conkeldurr", "Fighting"],
    535: ["Tympole", "Water"],
    536: ["Palpitoad", "Water/Ground"],
    537: ["Seismitoad", "Water/Ground"],
    538: ["Throh", "Fighting"],
    539: ["Sawk", "Fighting"],
    540: ["Sewaddle", "Bug/Grass"],
    541: ["Swadloon", "Bug/Grass"],
    542: ["Leavanny", "Bug/Grass"],
    543: ["Venipede", "Bug/Poison"],
    544: ["Whirlipede", "Bug/Poison"],
    545: ["Scolipede", "Bug/Poison"],
    546: ["Cottonee", "Grass/Fairy"],
    547: ["Whimsicott", "Grass/Fairy"],
    548: ["Petilil", "Grass"],
    549: ["Lilligant", "Grass"],
    550: ["Basculin", "Water"],
    551: ["Sandile", "Ground/Dark"],
    552: ["Krokorok", "Ground/Dark"],
    553: ["Krookodile", "Ground/Dark"],
    554: ["Darumaka", "Fire"],
    555: ["Darmanitan", "Fire"],
    556: ["Maractus", "Grass"],
    557: ["Dwebble", "Bug/Rock"],
    558: ["Crustle", "Bug/Rock"],
    559: ["Scraggy", "Dark/Fighting"],
    560: ["Scrafty", "Dark/Fighting"],
    561: ["Sigilyph", "Psychic/Flying"],
    562: ["Yamask", "Ghost"],
    563: ["Cofagrigus", "Ghost"],
    564: ["Tirtouga", "Water/Rock"],
    565: ["Carracosta", "Water/Rock"],
    566: ["Archen", "Rock/Flying"],
    567: ["Archeops", "Rock/Flying"],
    568: ["Trubbish", "Poison"],
    569: ["Garbodor", "Poison"],
    570: ["Zorua", "Dark"],
    571: ["Zoroark", "Dark"],
    572: ["Minccino", "Normal"],
    573: ["Cinccino", "Normal"],
    574: ["Gothita", "Psychic"],
    575: ["Gothorita", "Psychic"],
    576: ["Gothitelle", "Psychic"],
    577: ["Solosis", "Psychic"],
    578: ["Duosion", "Psychic"],
    579: ["Reuniclus", "Psychic"],
    580: ["Ducklett", "Water/Flying"],
    581: ["Swanna", "Water/Flying"],
    582: ["Vanillite", "Ice"],
    583: ["Vanillish", "Ice"],
    584: ["Vanilluxe", "Ice"],
    585: ["Deerling", "Normal/Grass"],
    586: ["Sawsbuck", "Normal/Grass"],
    587: ["Emolga", "Electric/Flying"],
    588: ["Karrablast", "Bug"],
    589: ["Escavalier", "Bug/Steel"],
    590: ["Foongus", "Grass/Poison"],
    591: ["Amoonguss", "Grass/Poison"],
    592: ["Frillish", "Water/Ghost"],
    593: ["Jellicent", "Water/Ghost"],
    594: ["Alomomola", "Water"],
    595: ["Joltik", "Bug/Electric"],
    596: ["Galvantula", "Bug/Electric"],
    597: ["Ferroseed", "Grass/Steel"],
    598: ["Ferrothorn", "Grass/Steel"],
    599: ["Klink", "Steel"],
    600: ["Klang", "Steel"],
    601: ["Klinklang", "Steel"],
    602: ["Tynamo", "Electric"],
    603: ["Eelektrik", "Electric"],
    604: ["Eelektross", "Electric"],
    605: ["Elgyem", "Psychic"],
    606: ["Beheeyem", "Psychic"],
    607: ["Litwick", "Ghost/Fire"],
    608: ["Lampent", "Ghost/Fire"],
    609: ["Chandelure", "Ghost/Fire"],
    610: ["Axew", "Dragon"],
    611: ["Fraxure", "Dragon"],
    612: ["Haxorus", "Dragon"],
    613: ["Cubchoo", "Ice"],
    614: ["Beartic", "Ice"],
    615: ["Cryogonal", "Ice"],
    616: ["Shelmet", "Bug"],
    617: ["Accelgor", "Bug"],
    618: ["Stunfisk", "Ground/Electric"],
    619: ["Mienfoo", "Fighting"],
    620: ["Mienshao", "Fighting"],
    621: ["Druddigon", "Dragon"],
    622: ["Golett", "Ground/Ghost"],
    623: ["Golurk", "Ground/Ghost"],
    624: ["Pawniard", "Dark/Steel"],
    625: ["Bisharp", "Dark/Steel"],
    626: ["Bouffalant", "Normal"],
    627: ["Rufflet", "Normal/Flying"],
    628: ["Braviary", "Normal/Flying"],
    629: ["Vullaby", "Dark/Flying"],
    630: ["Mandibuzz", "Dark/Flying"],
    631: ["Heatmor", "Fire"],
    632: ["Durant", "Bug/Steel"],
    633: ["Deino", "Dark/Dragon"],
    634: ["Zweilous", "Dark/Dragon"],
    635: ["Hydreigon", "Dark/Dragon"],
    636: ["Larvesta", "Bug/Fire"],
    637: ["Volcarona", "Bug/Fire"],
    638: ["Cobalion", "Steel/Fighting"],
    639: ["Terrakion", "Rock/Fighting"],
    640: ["Virizion", "Grass/Fighting"],
    641: ["Tornadus", "Flying"],
    642: ["Thundurus", "Electric/Flying"],
    643: ["Reshiram", "Dragon/Fire"],
    644: ["Zekrom", "Dragon/Electric"],
    645: ["Landorus", "Ground/Flying"],
    646: ["Kyurem", "Dragon/Ice"],
    647: ["Keldeo", "Water/Fighting"],
    648: ["Meloetta", "Normal/Psychic"],
    649: ["Genesect", "Bug/Steel"],    # Gen 4 ends here
}
pokeys = list(pokemon.keys())

Gen1_keys = pokeys[1-1:151]  # 1-151
Gen2_keys = pokeys[152-1:251]  # 152-251
Gen3_keys = pokeys[252-1:386]  # 252-386
Gen4_keys = pokeys[387-1:493]  # 387-493
'''
Gen5_keys = pokeys[494-1:649]  # 494-649
Gen6_keys = pokeys[650-1:721]  # 650-721
Gen7_keys = pokeys[722-1:809]  # 722-809
Gen8_keys = pokeys[810-1:905]  # 810-905
Gen9_keys = pokeys[906-1:1025]  # 906-1025
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
        elif pokeys[252-1] <= pokeys[index] <= pokeys[386-1]:
            print("Generation III")
        elif pokeys[387-1] <= pokeys[index] <= pokeys[493-1]:
            print("Generation IV")
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
            elif pokeys[int(inp) - 1] in Gen3_keys:
                print("Generation III")
            elif pokeys[int(inp) - 1] in Gen4_keys:
                print("Generation IV")
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

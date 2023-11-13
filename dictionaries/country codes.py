# Alpha-2 codes (2 numbers) and Alpha-3 codes (3)
inp = input("Give me a country's 2-letter or 3-letter code and you will receive more info:\n")
inp = inp.upper()
A2codes = {'AF': ['Afghanistan', 'AFG', '.af'],
           'AX': ['Åland', 'ALA', '.ax'],
           'AL': ['Albania', 'ALB', '.al'],
           'DZ': ['Algeria', 'DZA', '.dz'],
           'AS': ['American Samoa', 'ASM', '.as'],
           'AD': ['Andorra', 'AND', '.ad'],
           }

if inp in A2codes:
    print(f"Name: {A2codes[inp][0]}, 3-letter code: {A2codes[inp][1]}, top-level domain: {A2codes[inp][2]}")

A3codes = {'AFG': ['Afghanistan', 'AF', '.af'],
           'ALA': ['Åland', 'AX', '.ax'],
           'ALB': ['Albania', 'AL', '.al'],
           'DZA': ['Algeria', 'DZ', '.dz'],
           'ASM': ['American Samoa', 'AS', '.as'],
           'AND': ['Andorra', 'AD', '.ad'],
           }

if inp in A3codes:
    print(f"Name: {A3codes[inp][0]}, 2-letter code: {A3codes[inp][1]}, top-level domain: {A3codes[inp][2]}")

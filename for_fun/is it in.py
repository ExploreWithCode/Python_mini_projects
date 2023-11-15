inp = input('Type something: ')
word = []
if 'H' in inp or 'h' in inp:
    word.append('H')
    if 'E' in inp or 'e' in inp:
        word.append('e')
        print(f'Your input contains the letters to form "{word[0]+word[1]}" (Helium).')
else:
    print("Your input doesn't have what I need to create the mystery word.")

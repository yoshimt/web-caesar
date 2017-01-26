def alphabet_position(letter):
    alphabet = ('abcdefghijklmnopqrstuvwxyz')
    alphabetu = alphabet.upper()
    if letter in alphabet:
        letter = alphabet.index(letter)
        return letter
    elif letter in alphabetu:
        letter = alphabetu.index(letter)
        return letter


def rotate_character(char, rot):
    alphabet = ('abcdefghijklmnopqrstuvwxyz')
    alphabetu = alphabet.upper()
    x = alphabet_position(char)
    new_index = ''
    if char.isalpha() == True:
        new_char = (x + rot) % 26
        new_index = new_index + alphabet[new_char]
        if char.isupper():
            return new_index.upper()
        else:
            return new_index.lower()
        return new_index
    else:
        return char

def encrypt(text, rot):
    letter = ''
    for item in text:
        item = rotate_character(item, rot)
        letter = letter + item
    return letter

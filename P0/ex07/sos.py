import sys

MORSE_CODE_DICT = {' ': '/',
                   'A': '.-',
                   'B': '-...',
                   'C': '-.-.',
                   'D': '-..',
                   'E': '.',
                   'F': '..-.',
                   'G': '--.',
                   'H': '....',
                   'I': '..',
                   'J': '.---',
                   'K': '-.-',
                   'L': '.-..',
                   'M': '--',
                   'N': '-.',
                   'O': '---',
                   'P': '.--.',
                   'Q': '--.-',
                   'R': '.-.',
                   'S': '...',
                   'T': '-',
                   'U': '..-',
                   'V': '...-',
                   'W': '.--',
                   'X': '-..-',
                   'Y': '-.--',
                   'Z': '--..',
                   '1': '.----',
                   '2': '..---',
                   '3': '...--',
                   '4': '....-',
                   '5': '.....',
                   '6': '-....',
                   '7': '--...',
                   '8': '---..',
                   '9': '----.',
                   '0': '-----', }


def match(c):
    """
    associe un caractère à sa valeur dans le dictionnaire
    raise une erreur si le caractère n'y est pas
    """
    if MORSE_CODE_DICT.get(c):
        return MORSE_CODE_DICT.get(c)
    else:
        raise AssertionError()


def main():
    try:
        if len(sys.argv) != 2:
            raise AssertionError()
        try:
            arg = sys.argv[1].upper()
        except ValueError:
            raise AssertionError()
        myList = [MORSE_CODE_DICT[c] for c in arg if match(c)]
        print(myList)
        delimiter = ' '
        ret = delimiter.join(myList)
        print(ret)
    except AssertionError:
        print("AssertionError: the arguments are bad")


if __name__ == "__main__":
    main()

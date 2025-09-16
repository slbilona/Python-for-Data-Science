import sys
import string


def count_digits(s):
    """ compte les chiffres dans une string"""
    return sum(c.isdigit() for c in s)


def count_lower_letters(s):
    """compte les lettre minuscules dans une string"""
    return sum(c.islower() for c in s)


def count_upper_letters(s):
    """compte les lettre majuscules dans une string"""
    return sum(c.isupper() for c in s)


def count_punctuation_letters(s):
    """compte la ponctuation dans une string"""
    return sum(1 for c in s if c in string.punctuation)


def count_space_letters(s):
    """compte les espaces dans une string"""
    return sum(c.isspace() for c in s)


def main():
    try:
        argument = ""
        if len(sys.argv) > 2:
            raise AssertionError("more than one argument is provided")
        if len(sys.argv) < 2:
            while len(argument) == 0:
                print("What is the text to count?")
                argument = input()
        else:
            argument = sys.argv[1]
        print("The text contains", len(argument), "characters:")
        print(count_upper_letters(argument), "upper letters")
        print(count_lower_letters(argument), "lower letters")
        print(count_punctuation_letters(argument), "punctuation marks")
        print(count_space_letters(argument), "spaces")
        print(count_digits(argument), "digits")
    except AssertionError as error:
        print("AssertionError:", error)


if __name__ == "__main__":
    main()

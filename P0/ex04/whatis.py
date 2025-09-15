import sys

def main():
    try:
        if len(sys.argv) > 2:
            raise AssertionError ("more than one argument is provided")
        elif len(sys.argv) < 2:
            raise AssertionError ("less than one argument is provided")
        try:
            arg = sys.argv[1]
            chiffre = int(arg)
        except:
            raise AssertionError ("argument is not an integer")
        if (chiffre %2):
            print("I'm Odd.")
        else:
            print("I'm Even.")
    except AssertionError as error :
        print("AssertionError:", error)

main()
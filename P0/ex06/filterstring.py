from ft_filter import ft_filter
import sys


def main():
    try:
        try:
            s = sys.argv[1]
            n = int(sys.argv[2])
        except IndexError:
            raise AssertionError()
        except ValueError:
            raise AssertionError()
        myList = [word for word in s.strip().split(' ') if word != '']
        myList = ft_filter(lambda word: len(word) > n, myList)
        print(myList)
    except AssertionError:
        print("AssertionError: the arguments are bad")


if __name__ == "__main__":
    main()

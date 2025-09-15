from ft_filter import ft_filter
import sys


def main():
    s = sys.argv[1]
    try:
        n = int(sys.argv[2])
    except:
        raise ("n must be an integer")
    myList = s.split()
    print(myList)
    myList = ft_filter(lambda word: len(word) > n, myList)
    print(myList)


if __name__ == "__main__":
    main()

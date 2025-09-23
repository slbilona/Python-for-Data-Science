from load_csv import load


def main():
    try:
        print(load("life_expectancy_years.csv"))
    except Exception as error:
        print("error :", error)


if __name__ == "__main__":
    main()

from load_csv import load
import matplotlib.pyplot as plt
import pandas as pd


def main():
    try:
        df = load("life_expectancy_years.csv")
        print(df.shape)
        print(df.head())
        france_row = df[df["country"] == "France"]
        france_data = france_row.drop(columns=["country"]).iloc[0]
        years = france_data.index.astype(int)
        life_expectancy = france_data.values.astype(float)
        plt.plot(years, life_expectancy, label="France", color="blue")
        plt.title("France Life Expectancy Projections")
        plt.xlabel("Year")
        plt.ylabel("Life Expectancy")
        plt.legend()
        plt.show()
    except Exception as error:
        print("error :", error)


if __name__ == "__main__":
    main()

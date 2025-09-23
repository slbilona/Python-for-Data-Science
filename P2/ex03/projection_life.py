from load_csv import load
import matplotlib.pyplot as plt
import pandas as pd


def main():
    try:
        df = load("population_total.csv")
        france_row = df[df["country"] == "France"]
        belgique_row = df[df["country"] == "Belgium"]
        france_data = france_row.drop(columns=["country"]).iloc[0]
        belgique_data = belgique_row.drop(columns=["country"]).iloc[0]
        years_france = france_data.index.astype(int)
        years_belgique = belgique_data.index.astype(int)
        values_num_france = [float(v.replace("M", "")) for v in france_data.values]
        values_num_belgique = [float(v.replace("M", "")) for v in belgique_data.values]
        plt.plot(years_france, values_num_france, label="France", color="blue")
        plt.plot(years_belgique, values_num_belgique, label="Belgique", color="pink")
        plt.title("Population Projections")
        plt.xlabel("Year")
        plt.ylabel("Population")
        plt.legend()
        plt.xlim(min(years_belgique), 2050)
        plt.show()
    except Exception as error:
        print("error :", error)


if __name__ == "__main__":
    main()
from load_csv import load
import matplotlib.pyplot as plt
import pandas as pd
from matplotlib.ticker import ScalarFormatter


def main():
    try:
        df1 = load("income_per_person_gdppercapita_ppp_inflation_adjusted.csv")
        df2 = load("life_expectancy_years.csv")
        # Nettoyer les noms de colonnes (supprime les espaces invisibles)
        df1.columns = df1.columns.str.strip()
        df2.columns = df2.columns.str.strip()
        # Ne garder que 'country' + l'année 1900
        df1_1900 = df1[["country", "1900"]].rename(columns={"1900":
                                                            "gdp_1900"})
        df2_1900 = df2[["country", "1900"]].rename(columns={"1900":
                                                            "life_1900"})
        # Fusionner sur 'country'
        df_merged = pd.merge(df1_1900, df2_1900, on="country", how="inner")
        print(df_merged.head())
        plt.plot(df_merged["gdp_1900"], df_merged["life_1900"], 'o')
        plt.xlabel("Gross domestic product")
        plt.ylabel("Life expectancy")
        plt.title("1900")
        plt.xscale('log')
        plt.gca().xaxis.set_major_formatter(ScalarFormatter())
        plt.gca().xaxis.get_major_formatter().set_scientific(False)
        plt.show()
    except Exception as error:
        print("error :", error)


if __name__ == "__main__":
    main()

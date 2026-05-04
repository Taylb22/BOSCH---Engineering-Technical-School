import pandas as pd

path = "S:/COM/Human_Resources/01.Engineering_Tech_School/02.Internal/5 - Aprendizes/5 - Análise de dados/2 - Análise de dados 2025/Henrique dos Santos/Python/Bibliotecas Python/Pandas/Exercises/CSV/cat_breeds_clean.csv"

df = pd.read_csv(path, sep=";")

angora = df[df["Breed"] == "Angora"]
europe = df[df["Country"].isin(["France", "Germany", "UK"])]
black = df[df["Fur_colour_dominant"] == "black"]

ratio = df[df["Age_in_months"] > 6]
ratio["ratio"] = ratio["Weight"].div(df["Body_length"])

male = df[df["Gender"] == "male"][["Breed", "Age_in_months", "Weight", "Gender"]]

day_sleep = df[df["Breed"] == "Ragdoll"][["Breed", "Sleep_time_hours"]]
day_sleep["Percentage"] = round(day_sleep["Sleep_time_hours"].div(24).multiply(100), 2)
day_sleep = day_sleep.astype({"Percentage": str})
day_sleep["Percentage"] = day_sleep["Percentage"] + " %"

length = df["Body_length"].sum()

sleep_mean = df["Sleep_time_hours"].mean()

wei = df[(df["Age_in_months"] >= 3) & (df["Age_in_months"] <= 12)]["Weight"]

cm_age = df[((df["Fur_colour_dominant"] == "white") | (df["Fur_colour_dominant"] == "black"))
            & (df["Country"].isin(["USA", "Canada"]))]

cm_age["ratio"] = cm_age["Body_length"].div(cm_age["Age_in_months"])
cm_age = cm_age["ratio"].mean()

print(sleep_mean)
import pandas as pd

path = "S:/COM/Human_Resources/01.Engineering_Tech_School/02.Internal/5 - Aprendizes/5 - Análise de dados/2 - Análise de dados 2025/Henrique dos Santos/Python/Bibliotecas Python/Pandas/Exercises/CSV/tips.csv"

df = pd.read_csv(path, sep=";")

# df["tip_pct"] = round(df["tip"].div(df["total_bill"]).multiply(100), 2)
# df = df.sort_values(by="tip_pct", ascending=False)
# df["bad_tip"] = df[df["tip_pct"] < df["tip_pct"].mean()]["tip_pct"]

# gender = df[["sex", "tip"]].groupby("sex").mean()

# qty = df["servings"].sum()

# days = df[["day", "bad_tip"]].groupby("day").count().sort_values(by="bad_tip", ascending=False)
# days["pct"] = round(days["bad_tip"].div(days["bad_tip"].sum(), axis=0).multiply(100), 2)

# smokers = round(df[["smoker", "tip"]].groupby("smoker").mean(), 2)

aver = df[(df["servings"] > 3)
          & (df["time"] == "Dinner")
          & (df["smoker"] == "No")
          & (df["day"] == "Sat")]["tip"].mean()

# print(df)
# print()
# print(gender)
# print()
# print(qty)
# print()
# print(df["bad_tip"].dropna())
# print()
# print(days["pct"])
# print()
# print(smokers)
# print()
print(aver)
print()

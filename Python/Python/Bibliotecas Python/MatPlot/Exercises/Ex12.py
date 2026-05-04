import matplotlib.pyplot as plt
import pandas as pd

path = "S:/COM/Human_Resources/01.Engineering_Tech_School/02.Internal/5 - Aprendizes/5 - Análise de dados/2 - Análise de dados 2025/Henrique dos Santos/Python/Bibliotecas Python/MatPlot/CSV/he.csv"
df =pd.read_csv(path, sep=",")

df[df["is_corrective"] == 1]

df["end_date"] = pd.to_datetime(df["end_date"])
df = df.sort_values(by="end_date")

group = df.groupby(["responsible", "end_date"])["MachineId"].count().reset_index()
print(group)


# print(people)

dates = pd.DataFrame()
dates["end_date"] = df.end_date.unique()
# print(dates)

# aux = group[group["responsible"] == "Vanessa"]
# merged = pd.merge(dates, aux, on="end_date", how="outer")
# print(merged)

people = group["responsible"].unique()
for person in people:
    aux = group[group["responsible"] == person]
    aux = pd.merge(dates, aux, on="end_date", how="outer")
    aux["MachineId"] = aux.MachineId.fillna(0)
    aux["qty"] = aux.MachineId.cumsum()
    plt.plot(aux["end_date"], aux["qty"], label=person)

plt.legend()
plt.xticks(rotation=45)
plt.show()
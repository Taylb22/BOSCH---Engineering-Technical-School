import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("CSV/respiradores.csv", sep=",")

# x = df.MES
# y = df.TOTAL
# plt.bar(x, y, 0.6, align= "center", edgecolor="black")
# plt.title("COMPRA DE RESPIRADORES POR MÊS")
# plt.xticks(rotation = 90)
# plt.yticks(rotation = 45)
# plt.show()

# x = df.columns[1 : -1]
# y = df.sum()[1 : -1]

# plt.barh(x, y, 0.6, align="center", edgecolor="black", zorder=2)
# plt.title("COMPRA DE RESPIRADORES POR MÊS")
# plt.xticks(rotation = 90)
# plt.grid(zorder=0)
# plt.show()

fig, ax1 = plt.subplots(figsize=(10, 6))

bars = ax1.bar(df.MES, df.TOTAL, color="blue", label="Compras",
               edgecolor="black", align="center")
ax1.tick_params(axis='x', labelrotation=45)

df["MA_3"] = df["TOTAL"].rolling(window=3).mean()

ax1.plot(df.MES, df.MA_3, color="red")

plt.show()
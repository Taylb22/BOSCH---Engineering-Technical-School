import matplotlib.pyplot as plt
import pandas as pd

path = "../CSV/flights.csv"
df = pd.read_csv(path, sep=",")

plt.plot(df.year[df["month"] == "May"], df.passengers[df["month"] == "May"], marker="o")
plt.grid()

plt.show()
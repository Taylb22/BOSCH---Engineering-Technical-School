import pandas as pd
import matplotlib.pyplot as plt

path = "../CSV/cat_breeds_clean.CSV"
df = pd.read_csv(path, sep=";")

Width = df.groupby("Body_length")["Weight"].mean().reset_index()

plt.bar(Width.Body_length, Width.Weight)
plt.ylabel("Peso Médio")
plt.xlabel("Largura")

plt.show()
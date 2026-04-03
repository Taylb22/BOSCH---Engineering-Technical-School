import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

path = "../CSVs/car_ad.csv"

df = pd.read_csv(path, sep=",", encoding="latin-1")

df = df.value_counts("engType").reset_index()

plt.pie(df["count"], labels=df.engType, autopct="%1.1f%%")

plt.legend()
plt.show()
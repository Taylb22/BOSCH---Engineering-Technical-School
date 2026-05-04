import matplotlib.pyplot as plt
import pandas as pd

path = "../CSV/california_housing_train.csv"
df = pd.read_csv(path, sep=",")

plt.scatter(df["longitude"], df["latitude"], c=df["median_house_value"])
plt.show()
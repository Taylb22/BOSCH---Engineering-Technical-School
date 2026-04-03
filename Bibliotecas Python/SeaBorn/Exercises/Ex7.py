import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

path = "../../CSVs/tips.csv"

df = pd.read_csv(path, sep=';')

sns.catplot(data=df, x='day', y='tip', hue='sex', kind='violin', split=True)
plt.show()
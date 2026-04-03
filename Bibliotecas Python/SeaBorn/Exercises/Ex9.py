import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

path = "../../CSVs/tips.csv"

df = pd.read_csv(path, sep=';')

sns.catplot(data=df, kind='bar', x='day', y='total_bill', hue='sex')
plt.show()
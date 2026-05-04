import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

path = "../CSVs/tips.csv"

df = pd.read_csv(path, sep=";")

# sns.relplot(x='total_bill', y='tip',col='time' ,hue='day', row='sex',
#             size='servings' ,sizes=(10, 100) ,data=df)

sns.histplot(df["total_bill"], kde=True)

plt.show()
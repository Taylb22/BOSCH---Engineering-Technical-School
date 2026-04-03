import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

path = "../../CSVs/tips.csv"

df = pd.read_csv(path, sep=';')

sns.relplot(data=df, x='total_bill', y='tip', hue='day', size='servings', sizes=(10, 300))
plt.show()
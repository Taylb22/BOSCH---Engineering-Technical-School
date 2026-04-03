import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

path = "../../CSVs/tips.csv"

df = pd.read_csv(path, sep=';')

sns.histplot(data=df, x='total_bill', hue='sex', kde=True)
plt.show()
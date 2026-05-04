import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

path = "../../CSVs/penguins.csv"

df = pd.read_csv(path, sep=',')

sns.relplot(data=df, x='bill_length_mm', y='bill_depth_mm', hue="species", style='sex')
plt.show()
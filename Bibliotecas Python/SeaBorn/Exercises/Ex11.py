import matplotlib.pyplot as plt
import pandas as pd

path = "../../CSVs/all_stocks_5yr.csv"

SP = pd.read_csv(path, sep=',')
SP["date"] = pd.to_datetime(SP["date"], format='%Y-%m-%d')

SP.drop(columns=["Name"], inplace=True)
SP = SP.groupby("date").mean().reset_index().sort_values(by="date", ascending=True)
print(SP)

SP["MA_50"] = SP.close.rolling(window=50, min_periods=50).mean()
SP["MA_200"] = SP.close.rolling(window=200, min_periods=200).mean()

plt.plot(SP.date, SP.close, label="Close Value")
plt.plot(SP.date, SP.MA_50, label="MA_50", color="orange")
plt.plot(SP.date, SP.MA_200, label="MA_200", color="red")

plt.legend()
plt.show()
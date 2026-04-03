import matplotlib.pyplot as plt
import pandas as pd

path = "../CSV/netflix_titles.csv"
df = pd.read_csv(path, sep=",")

df = df.dropna()
df = df[(df["release_year"] >= 2015) & (df["release_year"] <= 2020) & (df["type"] == "Movie")]

fig, ax = plt.subplots(nrows=1, ncols=2, figsize=(12, 12))

US = df.groupby(["country", "release_year"]).count()["title"].reset_index()
US = US[US["country"] == "United States"]

ax[0].bar(US.release_year, US.title)

BR = df[df["country"] == "Brazil"]
BR["duration"] = BR["duration"].str.slice(0,-3).astype(int)
BR = BR.sort_values(by="duration", ascending=False).head(5)

ax[1].bar(BR.title, BR.duration)

ax[1].tick_params(axis='x', labelrotation=45)

plt.show()
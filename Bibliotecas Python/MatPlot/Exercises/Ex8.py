import matplotlib.pyplot as plt
import pandas as pd
import math as m

path = "../CSV/california_housing_train.csv"
df = pd.read_csv(path, sep=",")

# distancia² = (abs(latitude_LA - Latitude_X)² + (abs(Longitude_LA - Longitude_x))²)
#longitude latitude

df = df.astype({"longitude" : float,
                "latitude" : float})

df["distance_LA"] = (((df["latitude"] - 34.0)**2) + ((df["longitude"] - (-118.0))**2))**0.5
df["distance_SF"] = (((df["latitude"] - 37.0)**2) + ((df["longitude"] - (-122.0))**2))**0.5
df["distance_m"] = df[["distance_LA", "distance_SF"]].min(axis=1)

print(df[["distance_LA", "distance_SF", "distance_m" , "longitude", "latitude"]])

plt.scatter(df["distance_m"], df["median_house_value"])
plt.show()
import pandas as pd
import matplotlib.pyplot as plt

df1 = pd.read_csv("data/DS2_commodity_prices_10yr.csv")

df1["commodity"].value_counts().plot(kind="bar")

plt.title("Distribution of Commodities in DS2")
plt.xlabel("Commodity")
plt.ylabel("Count")

plt.show()
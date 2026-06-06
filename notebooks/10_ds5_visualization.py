import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("data/DS5_element_prices_monthly.csv")

df.groupby("element")["price_usd_per_kg"].mean().plot(kind="bar")
plt.title("Average Price per Element")
plt.xlabel("Element")
plt.ylabel("Average Price (USD/kg)")
plt.show()
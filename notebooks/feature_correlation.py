import pandas as pd

df = pd.read_csv("data/DS3_featured.csv")

corr = df.corr(numeric_only=True)

print(corr["condition_rating"]
      .sort_values(ascending=False))
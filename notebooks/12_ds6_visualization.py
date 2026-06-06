import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("data/DS6_historical_failures_2000.csv")

df["failure_mode"].value_counts().plot(kind="bar")
plt.title("Distribution of Failure Modes")
plt.xlabel("Failure Mode")
plt.ylabel("Count")
plt.show()
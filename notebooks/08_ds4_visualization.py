import pandas as pd
import matplotlib.pyplot as plt

df1 = pd.read_csv("data/DS4_crossdomain_features_daily.csv")
plt.scatter(df1["mqi"], df1["supply_disruption_prob"])
plt.title("MQI vs Supply Disruption Probability")
plt.xlabel("MQI")
plt.ylabel("Supply Disruption Probability")
plt.show()

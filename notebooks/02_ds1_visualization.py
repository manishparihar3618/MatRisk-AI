import pandas as pd
import matplotlib.pyplot as plt

df1 = pd.read_csv("data/DS1_material_properties_5500.csv")

df1["crystal_system"].value_counts().plot(kind="bar")

plt.title("Distribution of Crystal Systems in DS1")
plt.xlabel("Crystal System")
plt.ylabel("Count")

plt.show()
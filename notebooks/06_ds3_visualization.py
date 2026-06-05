import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv("data/DS3_infrastructure_bridges_5000.csv")


# Age vs Condition Rating
plt.figure(figsize=(8,5))
plt.scatter(df["age_years"], df["condition_rating"])
plt.xlabel("Age (Years)")
plt.ylabel("Condition Rating")
plt.title("Bridge Age vs Condition Rating")
plt.savefig("age_vs_condition_rating.png")
plt.close()

# Corrosion Rate vs Condition Rating
plt.figure(figsize=(8,5))
plt.scatter(df["corrosion_rate_mm_yr"], df["condition_rating"])
plt.xlabel("Corrosion Rate (mm/year)")
plt.ylabel("Condition Rating")
plt.title("Corrosion Rate vs Condition Rating")
plt.savefig("corrosion_rate_vs_condition_rating.png")
plt.close()

# Material Distribution
plt.figure(figsize=(8,5))
df["material"].value_counts().plot(kind="bar")
plt.xlabel("Material")
plt.ylabel("Number of Bridges")
plt.title("Distribution of Bridge Materials")
plt.savefig("material_distribution.png")
plt.close()


# # Structural Deficiency Distribution
# plt.figure(figsize=(6,4))
# df["structurally_deficient"].value_counts().plot(kind="bar")
# plt.xlabel("Structural Deficiency Status")
# plt.ylabel("Number of Bridges")
# plt.title("Structurally Deficient Bridges")
# plt.savefig("structural_deficiency_distribution.png")
# plt.close()


# print("Visualizations saved as PNG files in the current directory.")
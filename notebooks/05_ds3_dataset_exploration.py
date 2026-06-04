import pandas as pd

df1 = pd.read_csv("data/DS3_infrastructure_bridges_5000.csv")

print("Shape of the dataset:", df1.shape)
print("\nColumns in the dataset:", df1.columns)
print("\nFirst 5 rows of the dataset:", df1.head())
print("\nData types of each column:\n", df1.dtypes)
print("\nMissing values in each column:\n", df1.isnull().sum())
print("\nStatistical summary of the dataset:\n", df1.describe())
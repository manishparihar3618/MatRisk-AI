import pandas as pd

df = pd.read_csv("data/DS3_infrastructure_bridges_5000.csv")

df["age_utilization_ratio"] = (
    df["age_years"] /
    df["design_life_years"]
)

df["thickness_loss_ratio"] = (
    (df["original_thickness_mm"]
    - df["remaining_thickness_mm"])
    /
    df["original_thickness_mm"]
)

df["corrosion_exposure_score"] = (
    df["age_years"]
    * df["corrosion_rate_mm_yr"]
)

print(df.head())



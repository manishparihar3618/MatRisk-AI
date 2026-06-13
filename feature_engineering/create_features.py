import pandas as pd

df = pd.read_csv("data/DS3_infrastructure_bridges_5000.csv")

# Age utilization
df["age_utilization_ratio"] = (
    df["age_years"] / df["design_life_years"]
)

# Thickness loss
df["thickness_loss_ratio"] = (
    (df["original_thickness_mm"] - df["remaining_thickness_mm"])
    / df["original_thickness_mm"]
)

# Corrosion exposure
df["corrosion_exposure_score"] = (
    df["age_years"] * df["corrosion_rate_mm_yr"]
)

# Traffic stress
df["traffic_stress_score"] = (
    df["adt"] * df["age_years"]
)

# Remaining life
df["remaining_life_ratio"] = (
    (df["design_life_years"] - df["age_years"])
    / df["design_life_years"]
)

# Condition age risk
df["condition_age_risk"] = (
    df["age_years"] * (10 - df["condition_rating"])
)

# Fatigue stress
df["fatigue_stress_score"] = (
    df["fatigue_cycles_millions"] * df["adt"]
)

# Repair urgency
df["repair_urgency_score"] = (
    df["replacement_cost_M"] * df["structurally_deficient"]
)

df.to_csv("data/DS3_featured.csv", index=False)

print("DS3 features created")
print(df.shape)



 #### DS6 Features 

import pandas as pd

df = pd.read_csv("data/DS6_historical_failures_2000.csv")
severity_map = {
    "Low":1,
    "Medium":2,
    "High":3,
    "Critical":4
}

df["severity_num"] = df["severity"].map(severity_map)


df["severity_loss_score"] = (
    df["severity_num"] * df["loss_ratio"]
)

df["repair_impact_score"] = (
    df["repair_cost_USD"] * df["loss_ratio"]
)

df["failure_cost_ratio"] = (
    df["repair_cost_USD"]
    / df["replacement_value_USD"]
)

df["prediction_gap"] = (
    df["severity_num"]
    / (df["warning_lead_months"] + 1)
)

df["failure_risk_score"] = (
    df["severity_num"]
    * df["corrosion_rate_mm_yr"]
)

df.to_csv("data/DS6_featured.csv", index=False)
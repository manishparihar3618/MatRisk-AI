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

df["corrosion_adjusted_age"] = (df["age_years"]*df["corrosion_rate_mm_yr"])


df["traffic_stress_score"] = (df["adt"]*df["age_years"])


# df["strength_loss_proxy"] = (df["corrosion_rate_mm_yr"]/df["tensile_strength_Mpa"])


# df["durability_score"] = (
#     df["bulk_modulus_GPa"]
#     + df["shear_modulus_GPa"]
#     + df["melting_point_K"]
# )



# df["supply_risk_index"] = (
#     df["supply_disruption_prob"]
#     * df["herfindahl_index"]
# )


# df["replacement_risk"] = (
#     df["supply_disruption_prob"]
#     / (df["substitution_elasticity"] + 1e-6)
# )



# df["maintenance_inflation_risk"] = (
#     df["price_usd_per_kg"]
#     * abs(df["monthly_return"])
# )



# severity_map = {
#     "Low": 1,
#     "Medium": 2,
#     "High": 3,
#     "Critical": 4
# }

# df["severity_num"] = df["severity"].map(severity_map)

# df["severity_loss_score"] = (
#     df["severity_num"]
#     * df["loss_ratio"]
# )



# f["prediction_gap"] = (
#     df["severity_num"]
#     / (df["warning_lead_months"] + 1)
# )



# df["quality_risk_score"] = (
#     1 / (df["condition_rating"] + 1e-6)
# )



print(df.head())



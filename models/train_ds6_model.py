import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import r2_score

df = pd.read_csv("data/DS6_featured.csv")
df = df.dropna(subset=["failure_risk_score"])
target = "failure_risk_score"


X = df.drop(columns=[target])
y = df[target]


X = pd.get_dummies(X)

X = X.fillna(0)

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

model = RandomForestRegressor(
    n_estimators=100,
    random_state=42
)
model.fit(X_train, y_train)


preds = model.predict(X_test)
print("R2 Score:", r2_score(y_test, preds))
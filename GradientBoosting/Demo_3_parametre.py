import pandas as pd
from sklearn.ensemble import GradientBoostingRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error

# Simpelt syntetisk datasæt
data = {
    "Besøgende": [1000, 1500, 2000, 2500, 1200, 1800, 2200, 3000],
    "Regner": [1, 0, 1, 0, 0, 1, 0, 1],  # 1 for "Ja", 0 for "Nej"
    "Salg": [500, 700, 900, 1100, 600, 800, 1000, 1200],  # Måske i tusindvis af kroner
}

df = pd.DataFrame(data)

# Opdeling af data
X = df[["Besøgende", "Regner"]]
y = df["Salg"]
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.25, random_state=42
)

# Træning af Gradient Boosting model
model = GradientBoostingRegressor(
    n_estimators=100, learning_rate=0.1, max_depth=1, random_state=42
)
model.fit(X_train, y_train)

# Forudsigelse og evaluering
predictions = model.predict(X_test)
mse = mean_squared_error(y_test, predictions)

print(f"Mean Squared Error: {mse:.2f}")
print(f"Med saglg på:")
print(f"{X_test}, fås et salg på:")
print(f"{predictions}")

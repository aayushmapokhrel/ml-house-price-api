from sklearn.datasets import fetch_california_housing
from sklearn.ensemble import RandomForestRegressor
import joblib
import os

os.makedirs("app/ml", exist_ok=True)

data = fetch_california_housing(as_frame=True)

X = data.data[["MedInc", "HouseAge", "AveRooms", "Population"]]
y = data.target

model = RandomForestRegressor()
model.fit(X, y)


joblib.dump(model, "app/ml/model.pkl")
print("Model trained with 4 features")

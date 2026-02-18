import joblib
import numpy as np
import os

MODEL_PATH = "app/ml/model.pkl"

if not os.path.exists(MODEL_PATH):
    raise RuntimeError("Model not found. Run train_model.py first.")

model = joblib.load(MODEL_PATH)

def predict_price(input_data):
    data = np.array([[
        input_data.median_income, 
        input_data.house_age,      
        input_data.rooms,          
        input_data.population      
    ]])
    return float(model.predict(data)[0])

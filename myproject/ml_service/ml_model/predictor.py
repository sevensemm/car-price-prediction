import joblib
import pandas as pd
import os
from django.conf import settings
from catboost import CatBoostRegressor

model_path = os.path.join(settings.BASE_DIR, 'ml_service', 'ml_model', 'car_predict_model.cbm')
model_1 = CatBoostRegressor()
model_1.load_model(model_path)

correct_order = ['seller', 'vehicleType', 'gearbox', 'powerPS', 'model', 'kilometer', 'fuelType', 'brand', 'notRepairedDamage', 'nrOfPictures', 'age']

def predict_car_price(car_features):
    if isinstance(car_features, dict):
        car_features = pd.DataFrame([car_features])[correct_order]

    prediction = model_1.predict(car_features)
    return round(prediction[0], 2)
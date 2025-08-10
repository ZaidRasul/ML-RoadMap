from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import numpy as np

model = joblib.load("model.joblib")

class HouseFeatures(BaseModel):
    MedInc: float
    HouseAge: float
    AveRooms: float
    AveBedrms: float
    Population: float
    AveOccup: float
    Latitude: float
    Longitude: float

app = FastAPI(title="California Housing Price Prediction API")
@app.get("/")
def root():
    return {"message": "Welcome to the California Housing Price Prediction API"}

@app.post("/predict")
def predict(features: HouseFeatures):
    data = np.array([[features.MedInc, features.HouseAge, features.AveRooms,
                      features.AveBedrms, features.Population, features.AveOccup,
                      features.Latitude, features.Longitude]])
    
    # Predict 
    prediction = model.predict(data)[0]
    return {"predicted_price": float(prediction)}
    



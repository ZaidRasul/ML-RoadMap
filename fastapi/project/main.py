from fastapi import FastAPI
from pydantic import BaseModel
import joblib

model = joblib.load("model.joblib")
app = FastAPI(title="California Housing Price Prediction API")




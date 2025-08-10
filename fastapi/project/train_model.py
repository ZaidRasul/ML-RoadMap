import pandas as pd
from sklearn.datasets import fetch_california_housing
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
import joblib

# --- Load dataset ---
data_bunch = fetch_california_housing(as_frame=True)

# Create DataFrame (features + target)
df = pd.DataFrame(data_bunch.data, columns=data_bunch.feature_names)
df['MedHouseVal'] = data_bunch.target

# --- Explore dataset ---
print("Dataset Info:")
print(df.info())
print("\nDataset Stats:")
print(df.describe())

# --- Preprocess ---
# Drop rows with missing values (not expected in this dataset, but safe to include)
df = df.dropna()



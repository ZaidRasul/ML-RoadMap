import pandas as pd
import numpy as np
from sklearn.datasets import fetch_california_housing
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error, r2_score, mean_squared_error
import joblib

# --- Load dataset ---

#data = fetch_california_housing(as_frame=True)
#df = data.frame

data_bunch = fetch_california_housing(as_frame=True)
# Create DataFrame (features + target)
df = pd.DataFrame(data_bunch.data, columns=data_bunch.feature_names)
df['MedHouseVal'] = data_bunch.target

# --- Explore dataset ---
print("Dataset Info:")
print(df.info())
print("\nDataset Stats:")
print(df.describe())

# Drop rows with missing values
df = df.dropna()

#split 
X = df.drop('MedHouseVal', axis=1)
y = df['MedHouseVal']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# --- Train model ---
model = RandomForestRegressor(
    n_estimators=50,  
    max_depth=10,     
    random_state=42
)
model.fit(X_train, y_train)


# --- Evaluate ---
y_pred = model.predict(X_test)
print("\nModel Performance:")
print("MAE:", mean_absolute_error(y_test, y_pred))
print("RMSE:", np.sqrt(mean_squared_error(y_test, y_pred)))
print("R2:", r2_score(y_test, y_pred))

# --- Save model ---
joblib.dump(model, "model.joblib", compress=3)
print("\nModel saved as 'model.joblib'")
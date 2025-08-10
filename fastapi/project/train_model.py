import pandas as pd
from sklearn.datasets import fetch_california_housing
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error, r2_score, root_mean_squared_error
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

# --- Split ---
X = df.drop('MedHouseVal', axis=1)
y = df['MedHouseVal']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# --- Train model ---
model = RandomForestRegressor(random_state=42)
model.fit(X_train, y_train)



import os
import json
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

data_file = "Indian_crop_production_yield_dataset.csv"
data = pd.read_csv(data_file)

print("\n First 5 rows of data:")
print(data.head())

data = data.dropna()

categorical_cols = ['State_Name','District_Name','Season','Crop']
data = pd.get_dummies(data, columns=categorical_cols, drop_first=True)

print("\n Data after encoding:")
print(data.head())

X = data.drop("yield", axis=1)  
y = data["yield"]                

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

model = LinearRegression()
model.fit(X_train, y_train)

y_pred = model.predict(X_test)

print("\nR2 Score:", r2_score(y_test, y_pred))
print("MSE:", mean_squared_error(y_test, y_pred))

plt.figure(figsize=(6,6))
plt.scatter(y_test, y_pred, color="green", alpha=0.6, edgecolors="black")
plt.xlabel("Actual Yield")
plt.ylabel("Predicted Yield")
plt.title("🌱 Crop Yield Prediction")
plt.plot([y.min(), y.max()], [y.min(), y.max()], "r--")  # line y=x
plt.show()

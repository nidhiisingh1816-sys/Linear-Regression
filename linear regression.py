import numpy as np
from sklearn.linear_model import LinearRegression

# Sample data (X = input, y = output)
X = np.array([[1], [2], [3], [4], [5]])
y = np.array([2, 4, 5, 4, 5])

# Create model
model = LinearRegression()

# Train model
model.fit(X, y)

# Predict value
prediction = model.predict([[6]])

print("Prediction for 6:", prediction)
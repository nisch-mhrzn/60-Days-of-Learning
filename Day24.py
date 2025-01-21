import numpy as np
from sklearn.linear_model import LinearRegression

# Sample input data
X = np.array([[1], [2], [3], [4], [5]])
y = np.array([2, 4, 6, 8, 10])

# Create a linear regression model
model = LinearRegression()

# Train the model
model.fit(X, y)

# Predict the output for a new input
new_X = np.array([[6]])
predicted_y = model.predict(new_X)

print("Predicted output:", predicted_y)
# Evaluate the model
r_squared = model.score(X, y)
print("R-squared:", r_squared)

# Visualize the regression line
import matplotlib.pyplot as plt

plt.scatter(X, y, color='blue')
plt.plot(X, model.predict(X), color='red')
plt.xlabel('X')
plt.ylabel('y')
plt.title('Linear Regression')
plt.show()
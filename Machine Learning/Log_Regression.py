import numpy as np
from sklearn.model_selection import train_test_split

class MyLogisticRegression:
    def __init__(self, learning_rate=0.01, n_iterations=1000):
        self.learning_rate = learning_rate
        self.n_iterations = n_iterations
        self.weights = None
        self.bias = None

    def _sigmoid(self, z):
        return 1 / (1 + np.exp(-z))

    def fit(self, X, y):
        # Initialize parameters
        n_samples, n_features = X.shape
        self.weights = np.zeros(n_features)
        self.bias = 0

        # Gradient Descent
        for _ in range(self.n_iterations):
            # Calculate the linear model
            linear_model = np.dot(X, self.weights) + self.bias
            # Apply the sigmoid function
            y_predicted = self._sigmoid(linear_model)

            # Calculate gradients
            dw = (1 / n_samples) * np.dot(X.T, (y_predicted - y))
            db = (1 / n_samples) * np.sum(y_predicted - y)

            # Update parameters
            self.weights -= self.learning_rate * dw
            self.bias -= self.learning_rate * db

    def predict_proba(self, X):
        linear_model = np.dot(X, self.weights) + self.bias
        return self._sigmoid(linear_model)

    def predict(self, X, threshold=0.5):
        y_predicted_probs = self.predict_proba(X)
        y_predicted_labels = [1 if p > threshold else 0 for p in y_predicted_probs]
        return np.array(y_predicted_labels)

class LogRegression:
    def __init__(self, input_data, max_iter = 5000, learning_rate = 0.01):
        self.max_iter = max_iter
        self.data = input_data
        self.learning_rate = learning_rate
        self.coeff = None
        self.bias = None
    
    def logit(z):
        return 1 / (1 + np.exp(-z))
    
    def fit(self):
        n_samples, n_features = X.shape
        self.coeff = np.zeros(n_features)
        self.bias = 0
        for _ in range(self.max_iter):
            linear_model = np.dot(X, self.coeff) + self.bias
            y_predicted = self.logit(linear_model)
            dw =
            db = 
            self.coeff -= self.learning_rate * dw
            self.bias -= self.learning_rate * db
    
    def predict_proba(self, X):
        linear_model = np.dot(X, self.weights) + self.bias
        return self.logit(linear_model)
    
    def predit(self, X_new, threshold = 0.5):
        y_predicted_probs = self.predict_proba(X)
        y_predicted_labels = [1 if p > threshold else 0 for p in y_predicted_probs]
        return np.array(y_predicted_labels)
            
        
        

import numpy as np
from sklearn.model_selection import train_test_split

class MyLogisticRegression:
    

# Using the same sample data as before
X = np.array([0.5, 0.75, 1.0, 1.25, 1.5, 1.75, 2.0, 2.25, 2.5, 2.75, 3.0, 3.25, 3.5, 3.75, 4.0, 4.25, 4.5, 4.75, 5.0, 5.5]).reshape(-1, 1)
y = np.array([0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 1, 1, 1, 1, 1])

# Split data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Create and train the model
scratch_model = MyLogisticRegression(learning_rate=0.1, n_iterations=10000)
scratch_model.fit(X_train, y_train)

# Make predictions
predictions = scratch_model.predict(X_test)

# Calculate accuracy
accuracy = np.mean(predictions == y_test)
print(f"Model Accuracy (from scratch): {accuracy * 100:.2f}%")
import numpy as np
from collections import Counter

class KNN:
    """
    A K-Nearest Neighbors (KNN) classifier implemented from scratch.
    """

    def __init__(self, k=3):
        """
        Initializes the KNN classifier.

        Args:
            k (int): The number of nearest neighbors to consider for classification.
        """
        self.k = k

    def fit(self, X_train, y_train):
        """
        Stores the training data. KNN is a "lazy learner," so the fit method
        is very simple.

        Args:
            X_train (np.ndarray): The training input features.
            y_train (np.ndarray): The training target labels.
        """
        self.X_train = X_train
        self.y_train = y_train

    def _euclidean_distance(self, p1, p2):
        """
        Calculates the Euclidean distance between two points.
        """
        return np.sqrt(np.sum((p1 - p2)**2))

    def _predict_single(self, x):
        """
        Predicts the class label for a single data point.

        Args:
            x (np.ndarray): A single sample to classify.

        Returns:
            int: The predicted class label.
        """
        # 1. Calculate the distance from the new point to all training points
        distances = [self._euclidean_distance(x, x_train_point) for x_train_point in self.X_train]

        # 2. Get the indices of the k-nearest neighbors
        # We use np.argsort to get the indices that would sort the array
        k_nearest_indices = np.argsort(distances)[:self.k]

        # 3. Get the labels of the k-nearest neighbors
        k_nearest_labels = [self.y_train[i] for i in k_nearest_indices]

        # 4. Return the most common class label (majority vote)
        most_common = Counter(k_nearest_labels).most_common(1)
        return most_common[0][0]

    def predict(self, X_test):
        """
        Predicts class labels for a set of samples.

        Args:
            X_test (np.ndarray): The data to make predictions on.

        Returns:
            np.ndarray: The array of predicted class labels.
        """
        predictions = [self._predict_single(x) for x in X_test]
        return np.array(predictions)

class KNN:
    def __init__(self, X, Y, k = 3):
        self.k = k
        self.X_train = X
        self.Y_train = Y
    
    # for a single point
    def predict_single(self, x_new):
        dists = [np.sum((x_new - point))**2 for point in self.X_train]
        neighbor_index = np.argsort(dists)[:self.k]
        neighbor_label = self.Y_train[neighbor_index]
        x_label = Counter(neighbor_label).most_common(1) # return 1st most common label as tuple
        return x_label[0][0] # return this label
    
    # for a group of new data
    def predict(self, X_new):
        X_label = [self.predict_single(point) for point in X_new]
        return np.arrary(X_label)

class KNN:
    def __init__(self, X, Y, k = 3):
        self.k = k
        self.X_train = X
        self.Y_train = Y
    
    def predict_single(self, x_new):
        dists = [np.sum((x_new - point) ** 2) for point in self.X_train]
        neighbor_index = np.argsort(dists)[:self.k]
        neighbor_label = self.Y_train[neighbor_index]
        x_label = Counter(neighbor_label).most_common(1)
        return x_label[0][0]
    
    def predict(self, X_new):
        X_label = [self.predict_single(x_new) for x_new in X_new]
        return np.array(X_label)
        
    

# --- Demonstration ---
if __name__ == '__main__':
    from sklearn.model_selection import train_test_split
    from sklearn.datasets import make_classification
    
    # 1. Generate sample data
    X, y = make_classification(
        n_samples=200, 
        n_features=10, 
        n_informative=5, 
        n_redundant=2, 
        n_classes=3, # Multi-class example
        random_state=42
    )
    
    # 2. Split data into training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=123)
    
    # 3. Instantiate and use the model
    k_value = 5
    model = KNN(k=k_value)
    model.fit(X_train, y_train)
    
    # 4. Make predictions and evaluate
    predictions = model.predict(X_test)
    accuracy = np.mean(predictions == y_test)
    
    print("--- K-Nearest Neighbors from Scratch ---")
    print(f"Using k = {k_value}")
    print(f"Accuracy on test data: {accuracy:.4f}")
    print("--------------------------------------")


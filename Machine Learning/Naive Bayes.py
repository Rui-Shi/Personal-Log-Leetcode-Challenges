import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.datasets import make_classification

class NaiveBayes:
    """
    A Gaussian Naive Bayes classifier implemented from scratch.
    """

    def fit(self, X, y):
        """
        Trains the model by calculating priors, means, and variances for each class.

        Args:
            X (np.ndarray): Training input features. Shape: (n_samples, n_features).
            y (np.ndarray): Training target labels. Shape: (n_samples,).
        """
        n_samples, n_features = X.shape
        self._classes = np.unique(y)
        n_classes = len(self._classes)

        # Initialize priors, means, and variances
        self._priors = np.zeros(n_classes, dtype=np.float64)
        self._means = np.zeros((n_classes, n_features), dtype=np.float64)
        self._vars = np.zeros((n_classes, n_features), dtype=np.float64)

        for idx, c in enumerate(self._classes):
            # Get all samples belonging to the current class 'c'
            X_c = X[y == c]

            # 1. Calculate prior probability for class 'c'
            # P(c) = (number of samples in class c) / (total number of samples)
            self._priors[idx] = X_c.shape[0] / float(n_samples)

            # 2. Calculate mean and variance for each feature in class 'c'
            self._means[idx, :] = X_c.mean(axis=0)
            self._vars[idx, :] = X_c.var(axis=0)

    def _gaussian_pdf(self, class_idx, x):
        """
        Calculates the probability density of a sample 'x' for a given class,
        assuming a Gaussian distribution.

        Args:
            class_idx (int): The index of the class.
            x (np.ndarray): A single sample's features.

        Returns:
            np.ndarray: The log probability densities for each feature.
        """
        mean = self._means[class_idx]
        var = self._vars[class_idx]
        
        # Add a small constant to variance to avoid division by zero
        epsilon = 1e-9
        
        # Gaussian PDF formula: 1/sqrt(2*pi*var) * exp(-(x-mean)^2 / (2*var))
        numerator = np.exp(- (x - mean)**2 / (2 * var + epsilon))
        denominator = np.sqrt(2 * np.pi * var + epsilon)
        
        return numerator / denominator

    def _predict_single(self, x):
        """
        Predicts the class for a single sample.

        Args:
            x (np.ndarray): A single sample's features.

        Returns:
            int: The predicted class label.
        """
        posteriors = []

        # Calculate posterior probability for each class
        for idx, c in enumerate(self._classes):
            # Start with the log of the prior to prevent underflow
            prior = np.log(self._priors[idx])
            
            # Calculate the log of the likelihoods using the Gaussian PDF
            likelihoods = self._gaussian_pdf(idx, x)
            
            # The "naive" assumption allows us to sum the log-likelihoods
            # (which is equivalent to multiplying the probabilities)
            class_conditional = np.sum(np.log(likelihoods))
            
            # Posterior = Prior + Likelihood (in log space)
            posterior = prior + class_conditional
            posteriors.append(posterior)

        # Return the class with the highest posterior probability
        return self._classes[np.argmax(posteriors)]

    def predict(self, X):
        """
        Predicts class labels for a set of samples.

        Args:
            X (np.ndarray): The data to make predictions on.

        Returns:
            np.ndarray: The array of predicted class labels.
        """
        y_pred = [self._predict_single(x) for x in X]
        return np.array(y_pred)


# --- Demonstration ---
if __name__ == '__main__':
    # 1. Generate sample data
    X, y = make_classification(
        n_samples=500, n_features=10, n_informative=5, n_redundant=2, n_classes=2, random_state=42
    )

    # 2. Split data
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=123)

    # 3. Instantiate and train the model
    model = NaiveBayes()
    model.fit(X_train, y_train)

    # 4. Make predictions and evaluate
    predictions = model.predict(X_test)
    accuracy = np.mean(predictions == y_test)

    print("--- Naive Bayes from Scratch ---")
    print(f"Accuracy on test data: {accuracy:.4f}")
    print("--------------------------------")

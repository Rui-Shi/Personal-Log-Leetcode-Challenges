import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris

class PCA:
    """
    Principal Component Analysis (PCA) implemented from scratch.
    """

    def __init__(self, n_components):
        """
        Initializes the PCA transformer.

        Args:
            n_components (int): The number of principal components to keep.
        """
        self.n_components = n_components
        self.components = None  # Will store the principal components (eigenvectors)
        self.mean = None        # Will store the mean of the training data
        self.std = None         # Will store the standard deviation of the training data

    def fit(self, X):
        """
        Computes the principal components of the data.

        Args:
            X (np.ndarray): The training data of shape (n_samples, n_features).
        """
        # 1. Standardize the data (mean=0, std=1)
        self.mean = np.mean(X, axis=0)
        self.std = np.std(X, axis=0)
        # Add a small epsilon to std to avoid division by zero if a feature has zero variance
        epsilon = 1e-9
        X_std = (X - self.mean) / (self.std + epsilon)

        # 2. Calculate the covariance matrix
        # A covariance matrix is (X^T * X) / (n_samples - 1)
        # Note: np.cov expects features as rows, so we transpose X_std (X_std.T)
        cov_matrix = np.cov(X_std.T)

        # 3. Calculate eigenvalues and eigenvectors
        eigenvalues, eigenvectors = np.linalg.eig(cov_matrix)

        # The eigenvectors are columns of the matrix, so we need to transpose
        # to make them easier to work with as rows.
        eigenvectors = eigenvectors.T

        # 4. Sort eigenvectors by descending eigenvalues
        # We create pairs of (eigenvalue, eigenvector) and sort them
        idxs = np.argsort(eigenvalues)[::-1]
        eigenvalues = eigenvalues[idxs]
        eigenvectors = eigenvectors[idxs]

        # 5. Store the first n_components (the principal components)
        self.components = eigenvectors[0:self.n_components]

    def transform(self, X):
        """
        Projects the data onto the principal components.

        Args:
            X (np.ndarray): The data to transform.

        Returns:
            np.ndarray: The transformed data in the lower-dimensional space.
        """
        # Standardize the data using the mean and std from the fit step
        epsilon = 1e-9
        X_std = (X - self.mean) / (self.std + epsilon)

        # Project the data: dot product of the data and the principal components
        return np.dot(X_std, self.components.T)

class PCA:
    def __init__(self, n_comp):
        self.n_comp = n_comp
        self.comp
        self.mean = None
        self.var = None
        self.prin_comp = None
        self.eigenvectors = None
        self.eigenvalues = None
    
    def fit(self, X):
        self.mean = np.mean(X, axis=0)
        self.std = np.std(X, axis=0)
        X_std = (X - self.mean) / self.std
        cov_matrix = np.cov(X_std.T)
        eigenvalues, eigenvectors = np.linalg.eig(cov_matrix)
        index = np.argsort(eigenvalues)
        self.eigenvectors = eigenvectors[index]
        self.eigenvalues = eigenvalues[index]
        self.comp = self.eigenvectors[0:self.n_components]
        
    def transform(self, x_new):
        x_new_std = (x_new - self.mean) / self.std
        return x_new_std @ self.comp
        

# --- Demonstration ---
if __name__ == '__main__':
    # 1. Load a sample dataset
    # The Iris dataset has 4 features, making it a good candidate for reduction.
    iris = load_iris()
    X = iris.data
    y = iris.target

    # 2. Instantiate and use the PCA model
    # We will reduce the 4 features down to 2 principal components.
    pca = PCA(n_components=2)
    pca.fit(X)
    X_projected = pca.transform(X)

    # 3. Print the shape of the data before and after
    print("--- PCA from Scratch ---")
    print(f"Shape of original data: {X.shape}")
    print(f"Shape of transformed data: {X_projected.shape}")
    print("------------------------")

    # 4. Visualize the results
    plt.figure(figsize=(10, 7))
    pc1 = X_projected[:, 0]
    pc2 = X_projected[:, 1]
    
    scatter = plt.scatter(pc1, pc2, c=y, edgecolor='k', alpha=0.8, cmap=plt.cm.viridis)
    
    plt.title('PCA of Iris Dataset')
    plt.xlabel('Principal Component 1')
    plt.ylabel('Principal Component 2')
    plt.legend(handles=scatter.legend_elements()[0], labels=iris.target_names)
    plt.grid(True)
    plt.show()

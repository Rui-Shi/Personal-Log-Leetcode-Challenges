import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D # Required for 3D plotting

class MultipleLinearRegression:
    """
    A multiple linear regression model implemented from scratch using the
    Normal Equation (a direct analytical solution based on OLS).
    """

    def __init__(self):
        """
        Initializes the model. The coefficients will be learned during fitting.
        """
        self.coefficients = None # Will store bias (intercept) and weights

    def fit(self, X, y):
        """
        Trains the linear regression model using the Normal Equation.
        This is the matrix form of Ordinary Least Squares.

        Args:
            X (np.ndarray): Training input features. Shape: (n_samples, n_features).
            y (np.ndarray): Training target values. Shape: (n_samples,).
        """
        n_samples, n_features = X.shape
        
        # 1. Add intercept term (a column of ones) to X
        # This is the 'x0' term, which is always 1. It allows us to treat the
        # bias/intercept as just another weight in our coefficients vector.
        X_b = np.c_[np.ones((n_samples, 1)), X]

        # 2. Calculate coefficients using the Normal Equation
        # Formula: β = (X^T * X)^(-1) * X^T * y
        try:
            # Calculate the inverse of (X^T * X)
            xtx_inv = np.linalg.inv(X_b.T.dot(X_b))
            
            # Calculate X^T * y
            xty = X_b.T.dot(y)
            
            # Calculate the coefficients
            self.coefficients = xtx_inv.dot(xty)
            
        except np.linalg.LinAlgError:
            # This error occurs if the matrix is singular (not invertible),
            # which can happen if features are perfectly correlated.
            print("Error: Could not compute the inverse of X.T @ X. Features might be collinear.")
            self.coefficients = None


    def predict(self, X):
        """
        Makes predictions using the trained model.

        Args:
            X (np.ndarray): Input features for prediction. Shape: (n_samples, n_features).

        Returns:
            np.ndarray: The predicted values.
        """
        if self.coefficients is None:
            raise RuntimeError("The model has not been trained yet. Please call fit() first.")
            
        n_samples, n_features = X.shape
        
        # Add the same intercept term to the prediction data
        X_b = np.c_[np.ones((n_samples, 1)), X]
        
        # Make predictions by taking the dot product
        # y_pred = X_b * β
        return X_b.dot(self.coefficients)


class LinearRegression:
    def __init__(self, X, Y):
        self.X = X
        self.Y = Y
        self.coeff = None
    
    def fit(self):
        n_sample, _ = self.X.shape
        design = np.hstack(np.ones((n_sample, 1)), self.X)
        
        xtx_inv = np.linalg.inv(design.T.dot(design))
        xty = design.T.dot(self.Y)
        
        self.coeff = xtx_inv.dot(xty)
    
    def predict(self, X_new):
        if not self.coeff:
            print("Please call fit() to fit the model first")
        
        else:
            n_sample, _ = X_new.shape
            design_new = np.hstack(np.ones((n_sample, 1)), X_new)
            return design_new.dot(self.coeff)
            
        
        
        
# --- Demonstration ---
if __name__ == '__main__':
    # 1. Generate some sample 3D data
    # Let's create data that follows the plane y = 3*x1 + 4*x2 + 5
    np.random.seed(42) # for reproducibility
    n_samples = 100
    X1 = 2 * np.random.rand(n_samples, 1)
    X2 = 3 * np.random.rand(n_samples, 1)
    noise = np.random.randn(n_samples, 1)
    
    # Combine features into a single X matrix
    X = np.c_[X1, X2]
    
    # Calculate y based on the plane equation + noise
    y = 5 + (3 * X1) + (4 * X2) + noise
    y = y.ravel() # Flatten y to a 1D array

    # 2. Instantiate and train the model
    model = MultipleLinearRegression()
    model.fit(X, y)

    # 3. Print the learned coefficients
    print("--- Model Training Complete ---")
    if model.coefficients is not None:
        print(f"Learned Bias (b): {model.coefficients[0]:.4f}")
        print(f"Learned Weight for X1 (m1): {model.coefficients[1]:.4f}")
        print(f"Learned Weight for X2 (m2): {model.coefficients[2]:.4f}")
        print("(Original was b=5, m1=3, m2=4)")
    print("-----------------------------")

    # 4. Visualize the results in 3D
    fig = plt.figure(figsize=(12, 8))
    ax = fig.add_subplot(111, projection='3d')

    # Scatter plot of the original data points
    ax.scatter(X[:, 0], X[:, 1], y, color='blue', label='Original Data')

    # Create a meshgrid to plot the fitted plane
    x1_surf = np.arange(0, 2.1, 0.1)
    x2_surf = np.arange(0, 3.1, 0.1)
    x1_surf, x2_surf = np.meshgrid(x1_surf, x2_surf)
    
    # Predict z values (y) for the plane
    X_surf = np.c_[x1_surf.ravel(), x2_surf.ravel()]
    y_surf = model.predict(X_surf).reshape(x1_surf.shape)

    # Plot the fitted plane
    ax.plot_surface(x1_surf, x2_surf, y_surf, color='red', alpha=0.5, label='Fitted Plane')
    
    ax.set_xlabel('Feature X1')
    ax.set_ylabel('Feature X2')
    ax.set_zlabel('Target y')
    ax.set_title('Multiple Linear Regression Fit')
    plt.show()

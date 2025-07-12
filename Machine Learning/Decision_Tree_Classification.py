import numpy as np
from collections import Counter

class Node:
    """
    A class representing a single node in a decision tree.
    """
    def __init__(self, feature=None, threshold=None, left=None, right=None, *, value=None):
        """
        Initializes a node.

        Args:
            feature (int): The index of the feature to split on.
            threshold (float): The threshold value for the split.
            left (Node): The left child node (for samples where feature <= threshold).
            right (Node): The right child node (for samples where feature > threshold).
            value (int): The predicted class label if this is a leaf node.
        """
        self.feature = feature
        self.threshold = threshold
        self.left = left
        self.right = right
        self.value = value

    def is_leaf_node(self):
        """Checks if the node is a leaf node."""
        return self.value is not None


class DecisionTree:
    """
    A decision tree classifier implemented from scratch.
    """
    def __init__(self, min_samples_split=2, max_depth=100, n_features=None):
        """
        Initializes the Decision Tree.

        Args:
            min_samples_split (int): The minimum number of samples required to split a node.
            max_depth (int): The maximum depth of the tree.
            n_features (int): The number of features to consider for each split (for feature bagging).
                               If None, all features are considered.
        """
        self.min_samples_split = min_samples_split
        self.max_depth = max_depth
        self.n_features = n_features
        self.root = None

    def _entropy(self, y):
        """Calculates the entropy of a set of labels."""
        # Count occurrences of each class label
        hist = np.bincount(y)
        # Calculate probabilities
        ps = hist / len(y)
        # Calculate entropy
        return -np.sum([p * np.log2(p) for p in ps if p > 0])

    def _information_gain(self, y, X_column, threshold):
        """
        Calculates the information gain of a split.
        IG = Parent_Entropy - Weighted_Child_Entropy
        """
        # 1. Calculate parent entropy
        parent_entropy = self._entropy(y)

        # 2. Generate the split
        left_idxs = np.argwhere(X_column <= threshold).flatten()
        right_idxs = np.argwhere(X_column > threshold).flatten()
        
        # If a split doesn't divide the data, gain is 0
        if len(left_idxs) == 0 or len(right_idxs) == 0:
            return 0

        # 3. Calculate weighted average entropy of children
        n = len(y)
        n_l, n_r = len(left_idxs), len(right_idxs)
        e_l, e_r = self._entropy(y[left_idxs]), self._entropy(y[right_idxs])
        child_entropy = (n_l / n) * e_l + (n_r / n) * e_r

        # 4. Calculate information gain
        ig = parent_entropy - child_entropy
        return ig

    def _best_split(self, X, y, feat_idxs):
        """Finds the best feature and threshold to split on."""
        best_gain = -1
        split_idx, split_thresh = None, None

        for feat_idx in feat_idxs:
            X_column = X[:, feat_idx]
            # Consider all unique values in the column as potential thresholds
            thresholds = np.unique(X_column)
            for threshold in thresholds:
                gain = self._information_gain(y, X_column, threshold)
                if gain > best_gain:
                    best_gain = gain
                    split_idx = feat_idx
                    split_thresh = threshold
        
        return split_idx, split_thresh

    def _grow_tree(self, X, y, depth=0):
        """Recursively builds the decision tree."""
        n_samples, n_feats = X.shape
        n_labels = len(np.unique(y))

        # 1. Check stopping criteria
        if (depth >= self.max_depth or
            n_labels == 1 or
            n_samples < self.min_samples_split):
            # This is a leaf node
            leaf_value = Counter(y).most_common(1)[0][0]
            return Node(value=leaf_value)

        # Consider a random subset of features if n_features is set
        feat_idxs = np.random.choice(n_feats, self.n_features, replace=False) if self.n_features else np.arange(n_feats)

        # 2. Find the best split
        best_feat, best_thresh = self._best_split(X, y, feat_idxs)
        
        # If no split provides gain, create a leaf node
        if best_feat is None:
            leaf_value = Counter(y).most_common(1)[0][0]
            return Node(value=leaf_value)

        # 3. Create child nodes
        left_idxs = np.argwhere(X[:, best_feat] <= best_thresh).flatten()
        right_idxs = np.argwhere(X[:, best_feat] > best_thresh).flatten()
        
        left_child = self._grow_tree(X[left_idxs, :], y[left_idxs], depth + 1)
        right_child = self._grow_tree(X[right_idxs, :], y[right_idxs], depth + 1)
        
        return Node(best_feat, best_thresh, left_child, right_child)

    def _traverse_tree(self, x, node):
        """Recursively traverses the tree to predict a label for a single sample."""
        if node.is_leaf_node():
            return node.value

        if x[node.feature] <= node.threshold:
            return self._traverse_tree(x, node.left)
        else:
            return self._traverse_tree(x, node.right)

    def fit(self, X, y):
        """Builds the decision tree from training data."""
        # If n_features isn't specified, use all features
        self.n_features = X.shape[1] if not self.n_features else min(self.n_features, X.shape[1])
        self.root = self._grow_tree(X, y)

    def predict(self, X):
        """Predicts class labels for a set of samples."""
        return np.array([self._traverse_tree(x, self.root) for x in X])


# --- Demonstration ---
if __name__ == '__main__':
    from sklearn.model_selection import train_test_split
    from sklearn.datasets import make_classification
    
    # 1. Generate sample data
    X, y = make_classification(n_samples=500, n_features=10, n_informative=5, n_redundant=2, n_classes=2, random_state=42)
    
    # 2. Split data
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=123)
    
    # 3. Instantiate and train the model
    model = DecisionTree(max_depth=10)
    model.fit(X_train, y_train)
    
    # 4. Make predictions and evaluate
    predictions = model.predict(X_test)
    accuracy = np.mean(predictions == y_test)
    
    print("--- Decision Tree from Scratch ---")
    print(f"Accuracy on test data: {accuracy:.4f}")
    print("--------------------------------")
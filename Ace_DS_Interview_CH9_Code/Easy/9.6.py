def is_mirror(root):
    """
    Checks if a binary tree is a mirror of itself (i.e., symmetric around its center).

    Args:
        root: The root of the binary tree.

    Returns:
        True if the tree is a mirror, False otherwise.
    """
    if root is None:  # An empty tree is considered a mirror.
        return True
    return helper(root.left, root.right)  # Start the recursive check with left and right subtrees.

def helper(x, y):
    """
    Recursively checks if two subtrees are mirror images of each other.

    Args:
        x: The root of the first subtree.
        y: The root of the second subtree.

    Returns:
        True if the subtrees are mirror images, False otherwise.
    """
    if x is None and y is None:  # Base case: Both subtrees are empty, they are mirrors.
        return True
    elif x is None or y is None:  # If one subtree is empty and the other is not, they are not mirrors.
        return False
    else:  # Both subtrees are non-empty
        return (x.val == y.val and  # Check if root values are equal
                helper(x.left, y.right) and  # Recursively check if x's left subtree mirrors y's right subtree
                helper(x.right, y.left))   # Recursively check if x's right subtree mirrors y's left subtree
        
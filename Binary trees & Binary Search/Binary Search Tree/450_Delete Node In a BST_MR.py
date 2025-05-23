# Given a root node reference of a BST and a key, delete the node with the given key in the BST. Return the root node reference (possibly updated) of the BST.

# Basically, the deletion can be divided into two stages:

# Search for a node to remove.
# If the node is found, delete the node.
 

# Example 1:


# Input: root = [5,3,6,2,4,null,7], key = 3
# Output: [5,4,6,2,null,null,7]
# Explanation: Given key to delete is 3. So we find the node with value 3 and delete it.
# One valid answer is [5,4,6,2,null,null,7], shown in the above BST.
# Please notice that another valid answer is [5,2,6,null,4,null,7] and it's also accepted.

# Example 2:

# Input: root = [5,3,6,2,4,null,7], key = 0
# Output: [5,3,6,2,4,null,7]
# Explanation: The tree does not contain a node with value = 0.
# Example 3:

# Input: root = [], key = 0
# Output: []
 

# Constraints:

# The number of nodes in the tree is in the range [0, 104].
# -105 <= Node.val <= 105
# Each node has a unique value.
# root is a valid binary search tree.
# -105 <= key <= 105

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
import collections # For testing/printing tree

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def findMin(self, node: TreeNode) -> TreeNode:
        """
        Helper function to find the node with the minimum value
        in the subtree rooted at 'node'. In a BST, this is the
        leftmost node.
        """
        current = node
        while current and current.left:
            current = current.left
        return current

    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        """
        Deletes the node with the given key from the BST.
        Returns the root node reference (possibly updated).
        """
        # Base Case: If the tree/subtree is empty, return None.
        if not root:
            return None

        # 1. Search for the node to remove
        if key < root.val:
            # Key is smaller, go to the left subtree
            # Update the left child pointer with the result of the recursive call
            root.left = self.deleteNode(root.left, key)
        elif key > root.val:
            # Key is larger, go to the right subtree
            # Update the right child pointer with the result of the recursive call
            root.right = self.deleteNode(root.right, key)
        else:
            # Node found (key == root.val)! Now, delete it based on cases.

            # Case 1: Node is a leaf (no children) OR
            # Case 2: Node has only one child (right child)
            if not root.left:
                # Replace the current node with its right child (or None if leaf)
                temp = root.right
                # root = None # conceptually free the node (Python GC handles it)
                return temp # Return the right child to be the new node in parent's link

            # Case 2: Node has only one child (left child)
            elif not root.right:
                # Replace the current node with its left child
                temp = root.left
                # root = None
                return temp # Return the left child

            # Case 3: Node has two children
            else:
                # Find the in-order successor (smallest node in the right subtree)
                temp = self.findMin(root.right)

                # Copy the in-order successor's value to this node
                root.val = temp.val

                # Delete the in-order successor node from the right subtree
                # Note: The successor node itself will have at most one child (a right child)
                # so this recursive call will fall into Case 1 or Case 2 above.
                root.right = self.deleteNode(root.right, temp.val)

        # Return the root reference (it might be the same, or updated if the original root was deleted)
        return root

# --- Helper function for testing (converts tree to list level-order) ---
def treeToList(root: Optional[TreeNode]) -> List[Optional[int]]:
    if not root:
        return []
    result = []
    queue = collections.deque([root])
    while queue:
        node = queue.popleft()
        if node:
            result.append(node.val)
            # Important: Add children even if None, unless all subsequent nodes are also None
            # LeetCode style expects trailing nulls until the last actual node level
            queue.append(node.left)
            queue.append(node.right)
        else:
            result.append(None)
    # Remove trailing Nones
    while result and result[-1] is None:
        result.pop()
    return result

# --- Example Usage ---
# Example 1: Input: root = [5,3,6,2,4,null,7], key = 3
# Build the tree
root1 = TreeNode(5)
root1.left = TreeNode(3)
root1.right = TreeNode(6)
root1.left.left = TreeNode(2)
root1.left.right = TreeNode(4)
root1.right.right = TreeNode(7)

print(f"Example 1 - Initial Tree: {treeToList(root1)}")
solver = Solution()
new_root1 = solver.deleteNode(root1, 3)
print(f"Example 1 - Tree after deleting 3: {treeToList(new_root1)}") # Expected: [5, 4, 6, 2, null, null, 7] or [5, 2, 6, null, 4, null, 7]

# Example 2: Input: root = [5,3,6,2,4,null,7], key = 0
# Build the tree again
root2 = TreeNode(5)
root2.left = TreeNode(3)
root2.right = TreeNode(6)
root2.left.left = TreeNode(2)
root2.left.right = TreeNode(4)
root2.right.right = TreeNode(7)

print(f"\nExample 2 - Initial Tree: {treeToList(root2)}")
new_root2 = solver.deleteNode(root2, 0)
print(f"Example 2 - Tree after deleting 0: {treeToList(new_root2)}") # Expected: [5, 3, 6, 2, 4, null, 7]

# Example 3: Input: root = [], key = 0
root3 = None
print(f"\nExample 3 - Initial Tree: {treeToList(root3)}")
new_root3 = solver.deleteNode(root3, 0)
print(f"Example 3 - Tree after deleting 0: {treeToList(new_root3)}") # Expected: []



class Solution:
    def findMin(self, node: TreeNode) -> TreeNode:
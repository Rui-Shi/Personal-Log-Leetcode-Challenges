# Given an integer array nums where the elements are sorted in ascending order, convert it to a 
# height-balanced
#  binary search tree.

 

# Example 1:


# Input: nums = [-10,-3,0,5,9]
# Output: [0,-3,9,-10,null,5]
# Explanation: [0,-10,5,null,-3,null,9] is also accepted:

# Example 2:


# Input: nums = [1,3]
# Output: [3,1]
# Explanation: [1,null,3] and [3,1] are both height-balanced BSTs.
 

# Constraints:

# 1 <= nums.length <= 104
# -104 <= nums[i] <= 104
# nums is sorted in a strictly increasing order.


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        """
        Converts a sorted integer array into a height-balanced binary search tree.

        Args:
            nums: A sorted integer array (ascending order).

        Returns:
            The root node of the constructed height-balanced BST, or None if the input array is empty.
        """
        if not nums:  # Base case: Empty array
            return None

        mid = len(nums) // 2  # Find the middle index

        root = TreeNode(nums[mid])  # Create root node from the middle element
        root.left = self.sortedArrayToBST(nums[:mid])  # Recursively build left subtree
        root.right = self.sortedArrayToBST(nums[mid+1:])  # Recursively build right subtree, slicing won't return out of range error.

        return root
        
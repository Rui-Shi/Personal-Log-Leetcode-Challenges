# Given an integer n, return all the structurally unique BST's (binary search trees), which has exactly n nodes of unique values from 1 to n. Return the answer in any order.

 

# Example 1:


# Input: n = 3
# Output: [[1,null,2,null,3],[1,null,3,2],[2,1,3],[3,1,null,null,2],[3,2,null,1]]
# Example 2:

# Input: n = 1
# Output: [[1]]
 

# Constraints:

# 1 <= n <= 8


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


# Time and Space O(n * C_n)
from typing import List, Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def generateTrees(self, n: int) -> List[Optional[TreeNode]]:
        """
        Generates all structurally unique BSTs for values from 1 to n.
        """
        if n == 0:
            return []
        
        # memo is a cache to store results of generate(start, end)
        memo = {}

        def generate(start, end):
            # If the result is already cached, return it.
            if (start, end) in memo:
                return memo[(start, end)]

            # Base case: an empty range results in an empty subtree (None).
            # We return it in a list to allow the loops below to work correctly.
            if start > end:
                return [None]

            all_trees = []
            # Iterate through each number in the range to act as the root.
            for i in range(start, end + 1):
                # Generate all possible left subtrees.
                left_subtrees = generate(start, i - 1)
                
                # Generate all possible right subtrees.
                right_subtrees = generate(i + 1, end)
                
                # Combine each left subtree with each right subtree.
                for left_node in left_subtrees:
                    for right_node in right_subtrees:
                        root = TreeNode(i, left_node, right_node)
                        all_trees.append(root)
            
            # Cache the result before returning.
            memo[(start, end)] = all_trees
            return all_trees

        return generate(1, n)


 
class Solution:
    def generateTrees(self, n: int) -> List[Optional[TreeNode]]:
        # base case n = 0
        
        if n == 0:
            return []
        
        memo = {}
        
        def generate(start, end):
            
            if start > end:
                return [None]
            
            if (start, end) in memo:
                return memo[(start, end)]

            all_trees = []
            for i in range(start, end + 1):
                
                left_subtrees = generate(start, i - 1)
                right_subtrees = generate(i + 1, end)
                
                for left_subtree in left_subtrees:
                    for right_subtree in right_subtrees:
                        root = TreeNode(i, left_subtree, right_subtree)
                        all_trees.append(root)
            
            memo[(start, end)] = all_trees
            return all_trees
            
        return generate(1, n)
        
         
        
        
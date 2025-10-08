# Given the root of a binary tree and an integer targetSum, return all root-to-leaf paths where the sum of the node values in the path equals targetSum. Each path should be returned as a list of the node values, not node references.

# A root-to-leaf path is a path starting from the root and ending at any leaf node. A leaf is a node with no children.

 

# Example 1:


# Input: root = [5,4,8,11,null,13,4,7,2,null,null,5,1], targetSum = 22
# Output: [[5,4,11,2],[5,8,4,5]]
# Explanation: There are two paths whose sum equals targetSum:
# 5 + 4 + 11 + 2 = 22
# 5 + 8 + 4 + 5 = 22
# Example 2:


# Input: root = [1,2,3], targetSum = 5
# Output: []
# Example 3:

# Input: root = [1,2], targetSum = 0
# Output: []
 

# Constraints:

# The number of nodes in the tree is in the range [0, 5000].
# -1000 <= Node.val <= 1000
# -1000 <= targetSum <= 1000

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        if not root:
            return []
        
        res = []
        def backtracking_helper(cur_comb, node, targetSum):
            if not node.left and not node.right:
                if targetSum == 0:
                    res.append(cur_comb[:])
            
            elif node.left:
                backtracking_helper(cur_comb + [node.left.val], node.left, targetSum - node.left.val)
                
                if node.right: # backtracking
                    cur_comb.append(node.right.val)
                    backtracking_helper(cur_comb, node.right, targetSum - node.right.val)
            
            else:
                cur_comb.append(node.right.val)
                backtracking_helper(cur_comb, node.right, targetSum - node.right.val)
        
        backtracking_helper([root.val], root, targetSum - root.val)
        
        return res
    
# A better one:
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        res = []
        
        def dfs(node, remaining_sum, current_path):
            if not node:
                return

            # 1. Add current node to the path
            current_path.append(node.val)

            # 2. Check for a valid path at a leaf node
            if not node.left and not node.right and remaining_sum == node.val:
                # Add a *copy* of the path to results
                res.append(list(current_path))
            
            else:
                # 3. Recurse on children with the updated sum
                new_sum = remaining_sum - node.val
                dfs(node.left, new_sum, current_path)
                dfs(node.right, new_sum, current_path)

            # 4. Backtrack: remove the current node before returning
            # This is the crucial step that "undoes" the choice
            current_path.pop()

        # Start the process from the root
        dfs(root, targetSum, [])
        
        return res
                
                
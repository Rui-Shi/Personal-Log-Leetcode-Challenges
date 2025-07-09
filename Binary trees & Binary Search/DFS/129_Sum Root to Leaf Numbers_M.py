# You are given the root of a binary tree containing digits from 0 to 9 only.

# Each root-to-leaf path in the tree represents a number.

# For example, the root-to-leaf path 1 -> 2 -> 3 represents the number 123.
# Return the total sum of all root-to-leaf numbers. Test cases are generated so that the answer will fit in a 32-bit integer.

# A leaf node is a node with no children.

 

# Example 1:


# Input: root = [1,2,3]
# Output: 25
# Explanation:
# The root-to-leaf path 1->2 represents the number 12.
# The root-to-leaf path 1->3 represents the number 13.
# Therefore, sum = 12 + 13 = 25.
# Example 2:


# Input: root = [4,9,0,5,1]
# Output: 1026
# Explanation:
# The root-to-leaf path 4->9->5 represents the number 495.
# The root-to-leaf path 4->9->1 represents the number 491.
# The root-to-leaf path 4->0 represents the number 40.
# Therefore, sum = 495 + 491 + 40 = 1026.
 

# Constraints:

# The number of nodes in the tree is in the range [1, 1000].
# 0 <= Node.val <= 9
# The depth of the tree will not exceed 10.

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def dfs_helper(self, root, str_cur, nums):
        if not root:
            if str_cur:
                nums.append(int(str_cur))
            else:
                pass
        else:
            if not root.left and not root.right:
                nums.append(int(str_cur + str(root.val)))
            
            else: 
                if root.left:
                    self.dfs_helper(root.left, str_cur + str(root.val), nums)
                    
                if root.right:
                    self.dfs_helper(root.right, str_cur + str(root.val), nums)

    def sumNumbers(self, root: 'Optional[TreeNode]') -> int:
        nums = []
        self.dfs_helper(root, "", nums)
        print(nums)
        return sum(nums)


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        path_list = []
        
        def dfs_helper(node, path_cur):
            if not node:
                if path_cur:
                    path_list.append(int(path_cur))
            
            else:
                if not node.left and not node.right:
                    path_list.append(int(path_cur + str(node.val)))
                
                else:
                    if node.left:
                        dfs_helper(node.left, path_cur + str(node.val))
                    
                    if node.right:
                        dfs_helper(node.right, path_cur + str(node.val))
        
        dfs_helper(root, "")
        return sum(path_list)
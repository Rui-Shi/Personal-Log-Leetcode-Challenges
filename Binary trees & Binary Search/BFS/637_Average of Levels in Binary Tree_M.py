# Given the root of a binary tree, return the average value of the nodes on each level in the form of an array. Answers within 10-5 of the actual answer will be accepted.
 

# Example 1:


# Input: root = [3,9,20,null,null,15,7]
# Output: [3.00000,14.50000,11.00000]
# Explanation: The average value of nodes on level 0 is 3, on level 1 is 14.5, and on level 2 is 11.
# Hence return [3, 14.5, 11].
# Example 2:


# Input: root = [3,9,20,15,7]
# Output: [3.00000,14.50000,11.00000]
 

# Constraints:

# The number of nodes in the tree is in the range [1, 104].
# -231 <= Node.val <= 231 - 1


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# Time O(N)
# Space O(W) W: the max width of the tree
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        
        res = []
        def bfs_helper(node_list):
            nonlocal res
            
            next_level = []
            cur_val_list = []
            
            if node_list:
                for node in node_list:
                    cur_val_list.append(node.val)
                    
                    if node.left:
                        next_level.append(node.left)
                    if node.right:
                        next_level.append(node.right)
                    
                res.append(sum(cur_val_list)/len(cur_val_list))
                
                bfs_helper(list(next_level))
        
        bfs_helper([root])
        
        return res

import collections
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        if not root:
            return []
        
        res = []
        def bfs_helper(Node_List):
            q = collections.deque(Node_List)
            
            while q:
                n = len(q)
                cur_nodes_val = []
                for _ in range(n):
                    cur_node = q.popleft()
                    cur_nodes_val.append(cur_node.val)
                    
                    if cur_node.left:
                        q.append(cur_node.left)
                    if cur_node.right:
                        q.append(cur_node.right)
                    
                res.append(sum(cur_nodes_val)/n)
        
        bfs_helper([root])
        return res
            
            
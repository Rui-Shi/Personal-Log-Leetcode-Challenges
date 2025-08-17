# Given the root of a binary tree, return the zigzag level order traversal of its nodes' values. (i.e., from left to right, then right to left for the next level and alternate between).

 

# Example 1:


# Input: root = [3,9,20,null,null,15,7]
# Output: [[3],[20,9],[15,7]]
# Example 2:

# Input: root = [1]
# Output: [[1]]
# Example 3:

# Input: root = []
# Output: []
 

# Constraints:

# The number of nodes in the tree is in the range [0, 2000].
# -100 <= Node.val <= 100
# O(n) for space and time
import collections

class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        reverse = False
        res = []
        queue = collections.deque([root])

        if not root:
            return res
        
        while queue:
            n = len(queue)
            cur_level = []
            for i in range(n):
                cur_node = queue.popleft()
                cur_level.append(cur_node.val)
                
                if cur_node.left:
                    queue.append(cur_node.left)
                    
                if cur_node.right:
                    queue.append(cur_node.right)
            
            if reverse:
                res.append(cur_level[::-1])
            else:
                res.append(cur_level[:])
            
            reverse = not reverse
        return res
        
        
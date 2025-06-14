# Given a binary tree

# struct Node {
#   int val;
#   Node *left;
#   Node *right;
#   Node *next;
# }
# Populate each next pointer to point to its next right node. If there is no next right node, the next pointer should be set to NULL.

# Initially, all next pointers are set to NULL.

 

# Example 1:


# Input: root = [1,2,3,4,5,null,7]
# Output: [1,#,2,3,#,4,5,7,#]
# Explanation: Given the above binary tree (Figure A), your function should populate each next pointer to point to its next right node, just like in Figure B. The serialized output is in level order as connected by the next pointers, with '#' signifying the end of each level.
# Example 2:

# Input: root = []
# Output: []
 

# Constraints:

# The number of nodes in the tree is in the range [0, 6000].
# -100 <= Node.val <= 100

import collections

"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    """
    Populates the 'next' pointer for each node in a binary tree.

    The 'next' pointer should point to the node's immediate right neighbor
    on the same level. If there is no right neighbor, it should be None.
    """
    def connect(self, root: 'Node') -> 'Node':
        if not root:
            return root
        
        current_level = [root]
        
        while current_level:
            next_level = []
            for i, node in enumerate(current_level):
                if i == len(current_level) - 1:
                    pass
                else:
                    node.next = current_level[i + 1]
                
                if node.left:
                    next_level.append(node.left)
                    
                if node.right:
                    next_level.append(node.right)
                    
            current_level[:] = next_level
                
        return root


class Solution:
    def connect(self, root: 'Node') -> 'Node':
        
        if not root:
            return None # Handle empty tree case

        queue = collections.deque([root])

        while queue:
            level_size = len(queue)
            prev_node = None

            # Process all nodes at the current level
            for i in range(level_size):
                current_node = queue.popleft()

                # Link the previous node's 'next' to the current node
                if prev_node:
                    prev_node.next = current_node

                # Update the previous node for the next iteration
                prev_node = current_node

                # Add children to the queue for the next level's processing
                # Add left child first, then right, to maintain level order
                if current_node.left:
                    queue.append(current_node.left)
                if current_node.right:
                    queue.append(current_node.right)
        return root
                    
                    
                  
        
        
        
        
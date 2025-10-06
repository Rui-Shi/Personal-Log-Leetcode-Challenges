# Given the head of a singly linked list where elements are sorted in ascending order, convert it to a height-balanced binary search tree.

 

# Example 1:


# Input: head = [-10,-3,0,5,9]
# Output: [0,-3,9,-10,null,5]
# Explanation: One possible answer is [0,-3,9,-10,null,5], which represents the shown height balanced BST.
# Example 2:

# Input: head = []
# Output: []
 

# Constraints:

# The number of nodes in head is in the range [0, 2 * 104].
# -105 <= Node.val <= 105



# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# Time: O(NlogN)
# Space: O(N)
class Solution:
    def sortedListToBST(self, head: Optional[ListNode]) -> Optional[TreeNode]:
        if not head:
            return None
        
        # Linked list to Array time: O(N)
        num_list = []
        while head:
            num_list.append(head.val)
            head = head.next
        
        # At each level, the slicing takes O(N) time, and there are O(logN) levels.
        def build_tree(nums):
            
            n = len(nums)
            if n == 0:
                return None
            
            left, right = 0, n - 1
            
            mid = (left + right) // 2
            
            node = TreeNode(nums[mid])
            node.left = build_tree(nums[0:mid])
            node.right = build_tree(nums[(mid+1):n])
            return node
        
        return build_tree(num_list)
        
        
            
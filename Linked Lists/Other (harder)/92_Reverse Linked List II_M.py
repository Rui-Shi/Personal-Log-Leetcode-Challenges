# Given the head of a singly linked list and two integers left and right where left <= right, reverse the nodes of the list from position left to position right, and return the reversed list.

 

# Example 1:


# Input: head = [1,2,3,4,5], left = 2, right = 4
# Output: [1,4,3,2,5]
# Example 2:

# Input: head = [5], left = 1, right = 1
# Output: [5]

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        
        if not head.next or left == right:
            return head
        
        i = 1
        curr = head
        pre = ListNode() # dummy node
        
        while i < left:
            pre = curr
            curr = curr.next
            i += 1
            
        left_pre = pre
        left_node = curr
        
        pre = None
        
        while i <= right:
            next = curr.next
            curr.next = pre
            pre = curr
            curr = next
            i += 1
        
        right_node = pre
        right_next = curr
        
        left_pre.next = right_node
        left_node.next = right_next
    
        if left == 1:
            return left_pre.next
        else:
            return head
            
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        if left == right or not head.next:
            return head
        
        i = 1
        curr = head
        pre = ListNode()
        pre.next = curr
        
        while i < left:
            pre = curr
            curr = curr.next
            i += 1
        
        left_1 = pre
        left_2 = curr
        
        pre = curr
        curr = curr.next
        i += 1
        
        while i <= right:
            next = curr.next
            curr.next = pre
            pre = curr
            curr = next
            i += 1
        
        right_1 = pre
        right_2 = curr
        
        left_1.next = right_1
        left_2.next = right_2
        
        if left == 1:
            return right_1
        else:
            return head
            
            
            
            
        
        
        
    
            
            
            
        
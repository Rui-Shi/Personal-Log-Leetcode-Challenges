# Given the head of a linked list and a value x, partition it such that all nodes less than x come before nodes greater than or equal to x.

# You should preserve the original relative order of the nodes in each of the two partitions.

 

# Example 1:


# Input: head = [1,4,3,2,5,2], x = 3
# Output: [1,2,2,4,3,5]
# Example 2:

# Input: head = [2,1], x = 2
# Output: [1,2]
 

# Constraints:

# The number of nodes in the list is in the range [0, 200].
# -100 <= Node.val <= 100
# -200 <= x <= 200


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        less_head = ListNode(0)  # Head of the "less than x" list
        less_tail = less_head     # Tail of the "less than x" list

        greater_head = ListNode(0)  # Head of the "greater than or equal to x" list
        greater_tail = greater_head # Tail of the "greater than or equal to x" list

        while head:
            if head.val < x:
                less_tail.next = head  # Add to the "less than x" list
                less_tail = less_tail.next  # Move the tail
            else:
                greater_tail.next = head  # Add to the "greater than or equal to x" list
                greater_tail = greater_tail.next  # Move the tail

            head = head.next  # Move to the next node in the original list

        less_tail.next = greater_head.next  # Connect the two lists (crucial!)
        greater_tail.next = None # important so that there is no cycle in the linked list

        return less_head.next  # Return the head of the combined list
            
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        small_head = ListNode(0)
        small_tail = small_head
        
        large_head = ListNode(0)
        large_tail = large_head
        
        while head:
            if head.val < x:
                small_tail.next = ListNode(head.val)
                small_tail = small_tail.next
            
            else:
                large_tail.next = ListNode(head.val)
                large_tail = large_tail.next
            
            head = head.next
            
        small_tail.next = large_head.next
        large_tail.next = None
        
        return small_head.next
        
        
            
        
                
                
         
        
        
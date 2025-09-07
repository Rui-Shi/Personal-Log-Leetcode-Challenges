# Given the head of a sorted linked list, delete all duplicates such that each element appears only once. Return the linked list sorted as well.

 

# Example 1:


# Input: head = [1,1,2]
# Output: [1,2]
# Example 2:


# Input: head = [1,1,2,3,3]
# Output: [1,2,3]
 

# Constraints:

# The number of nodes in the list is in the range [0, 300].
# -100 <= Node.val <= 100
# The list is guaranteed to be sorted in ascending order.

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next: # Base Cases: empty list or single node
            return head
        if head.val == head.next.val:
            head.next = self.deleteDuplicates(head.next) # Remove duplicates from the rest, Simply calling self.deleteDuplicates(head.next) without assigning the return value does NO Modification
            return head.next if head.val == head.next.val else head # Handle cases where multiple consecutive duplicates are at the beginning
        
        else:
            head.next = self.deleteDuplicates(head.next) # No duplicate, process the rest of the list
            return head


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head
        
        cur = head
        while cur.next:
            if cur.val == cur.next.val:
                cur.next = cur.next.next
            
            else:
                cur = cur.next
        
        return head
            
            
# Given the head of a singly linked list, reverse the list, and return the reversed list.

 

# Example 1:


# Input: head = [1,2,3,4,5]
# Output: [5,4,3,2,1]
# Example 2:


# Input: head = [1,2]
# Output: [2,1]
# Example 3:

# Input: head = []
# Output: []

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]: # Optional[ListNode]: the input can be empty or ListNode
        prev = None
        curr = head
        while curr is not None:
            next_node = curr.next  # Save next node
            curr.next = prev  # Reverse the pointer
            prev = curr  # Move prev forward
            curr = next_node  # Move curr forward
        return prev


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]: # Optional[ListNode]: the input can be empty or ListNode
        prev = None
        cur = head
        while cur:
            next_node = cur.next
            cur.next = prev
            prev = cur
            cur = next_node
        return prev
    
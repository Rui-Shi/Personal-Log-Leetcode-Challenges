# Given the head of a linked list, remove the nth node from the end of the list and return its head.

 

# Example 1:


# Input: head = [1,2,3,4,5], n = 2
# Output: [1,2,3,5]
# Example 2:

# Input: head = [1], n = 1
# Output: []
# Example 3:

# Input: head = [1,2], n = 1
# Output: [1]

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        fast = head
        slow = head

        for i in range(n):
            fast = fast.next
        
        k = 0
        while fast:
            fast = fast.next
            previous_node = slow
            slow = slow.next
            next_node = slow.next
            k += 1
    
        if k == 0:
            return head.next

        previous_node.next = next_node
        return head


# A better version
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0)  # Create a dummy node
        dummy.next = head
        
        fast = head
        slow = head
        
        pre = dummy
        
        for i in range(n):
            fast = fast.next
            
        while fast:
            fast = fast.next
            pre = pre.next
            slow = slow.next  
        
        pre.next = slow.next
        
        return head          
        
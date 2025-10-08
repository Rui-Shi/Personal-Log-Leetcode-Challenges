# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# time: O(nlogn) # logn level for division, n for merging at each level
# Space: O(logn) for recursion stack, not strictly O(1)
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Base case: if the list is empty or has only one node, it's already sorted.
        if not head or not head.next:
            return head
        
        # 1. SPLIT the list into two halves.
        # We use the fast and slow pointer technique to find the middle.
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        # `mid` is the head of the second half of the list.
        mid = slow.next
        # Break the link to create two separate lists.
        slow.next = None
        
        # 2. CONQUER: Recursively sort each half.
        left_half = self.sortList(head)
        right_half = self.sortList(mid)
        
        # 3. COMBINE: Merge the two sorted halves.
        return self.merge(left_half, right_half)

    def merge(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        """Merges two sorted linked lists into one."""
        # Create a dummy node to serve as the starting point of the merged list.
        dummy = ListNode()
        tail = dummy
        
        # Compare nodes from both lists and append the smaller one.
        while l1 and l2:
            if l1.val < l2.val:
                tail.next = l1
                l1 = l1.next
            else:
                tail.next = l2
                l2 = l2.next
            tail = tail.next
        
        # Append the remaining nodes from whichever list is not yet empty.
        if l1:
            tail.next = l1
        else:
            tail.next = l2
            
        return dummy.next

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# time: O(nlogn)
# Space: O(logn) for recursion stack, not strictly O(1)
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Base case: if the list is empty or has only one node, it's already sorted.
        if not head or not head.next:
            return head
        
        # 1. SPLIT the list into two halves.
        # We use the fast and slow pointer technique to find the middle.
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        # `mid` is the head of the second half of the list.
        mid = slow.next
        # Break the link to create two separate lists.
        slow.next = None
        
        # 2. CONQUER: Recursively sort each half.
        left_half = self.sortList(head)
        right_half = self.sortList(mid)
        
        # 3. COMBINE: Merge the two sorted halves.
        return self.merge(left_half, right_half)

    def merge(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        """Merges two sorted linked lists into one."""
        # Create a dummy node to serve as the starting point of the merged list.
        dummy = ListNode()
        tail = dummy
        
        # Compare nodes from both lists and append the smaller one.
        while l1 and l2:
            if l1.val < l2.val:
                tail.next = l1
                l1 = l1.next
            else:
                tail.next = l2
                l2 = l2.next
            tail = tail.next
        
        # Append the remaining nodes from whichever list is not yet empty.
        if l1:
            tail.next = l1
        else:
            tail.next = l2
            
        return dummy.next


class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # base case
        if not head or not head.next:
            return head
        
        slow, fast = head, head.next
        
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        mid = slow.next
        slow.next = None
        
        left_half = self.sortList(head)
        right_half = self.sortList(mid)
        
        return self.merge(left_half, right_half)
    
    def merge(self, l1, l2):
        dummy = ListNode()
        pointer = dummy
        
        while l1 and l2:
            if l1.val < l2.val:
                pointer.next = l1
                l1 = l1.next
            
            else:
                pointer.next = l2
                l2 = l2.next
            
            pointer = pointer.next
                
        if l1:
            pointer.next = l1
        else:
            pointer.next = l2
        
        return dummy.next
        
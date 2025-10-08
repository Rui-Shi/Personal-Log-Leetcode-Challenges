# Given the head of a singly linked list, sort the list using insertion sort, and return the sorted list's head.

# The steps of the insertion sort algorithm:

# Insertion sort iterates, consuming one input element each repetition and growing a sorted output list.
# At each iteration, insertion sort removes one element from the input data, finds the location it belongs within the sorted list and inserts it there.
# It repeats until no input elements remain.
# The following is a graphical example of the insertion sort algorithm. 
# The partially sorted list (black) initially contains only the first element in the list. 
# One element (red) is removed from the input data and inserted in-place into the sorted list with each iteration.


 

# Example 1:


# Input: head = [4,2,1,3]
# Output: [1,2,3,4]
# Example 2:


# Input: head = [-1,5,3,4,0]
# Output: [-1,0,3,4,5]
 

# Constraints:

# The number of nodes in the list is in the range [1, 5000].
# -5000 <= Node.val <= 5000

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
        Sorts a singly linked list using the insertion sort algorithm.
        
        Args:
            head: The head of the singly linked list.
            
        Returns:
            The head of the sorted singly linked list.
        """
        
        # Base case: if the list is empty or has only one node, it's already sorted.
        if not head or not head.next:
            return head
        
        # Create a dummy node to serve as the start of the sorted list.
        # This simplifies inserting nodes at the beginning of the list.
        dummy = ListNode(0, head)
        
        # `last_sorted` points to the last node in the sorted part of the list.
        # `current` is the node we are considering inserting into the sorted part.
        last_sorted = head
        current = head.next
        
        while current:
            if current.val >= last_sorted.val:
                # If the current node is already in the correct order, just move on.
                last_sorted = last_sorted.next
            else:
                # The current node is smaller and needs to be moved.
                # Find the correct insertion point starting from the beginning.
                prev = dummy
                while prev.next.val <= current.val:
                    prev = prev.next
                
                # Unlink `current` from its original position.
                last_sorted.next = current.next
                
                # Insert `current` into its new correct position.
                current.next = prev.next
                prev.next = current
            
            # Move to the next node in the original list to be sorted.
            current = last_sorted.next
            
        return dummy.next


class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # base case, if the list has only one node or less
        
        if not head or not head.next:
            return head
        
        dummy = ListNode(0, head)
        
        last_sorted = head # the last node that is sorted
        cur = head.next
        
        while cur:
            if cur.val >= last_sorted.val: # the current node is already sorted
                last_sorted = cur
                
            else:
                pointer = dummy
                while cur.val > pointer.next.val:
                    pointer = pointer.next
                
                # unlink the current node
                last_sorted.next = cur.next
                
                # insert to new position
                cur.next = pointer.next
                pointer.next = cur
                
            cur = last_sorted.next
        
        return dummy.next
            
            
            
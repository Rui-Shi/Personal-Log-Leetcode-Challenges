# Given the head of a singly linked list, return the middle node of the linked list.

# If there are two middle nodes, return the second middle node.

 

# Example 1:


# Input: head = [1,2,3,4,5]
# Output: [3,4,5]
# Explanation: The middle node of the list is node 3.
# Example 2:


# Input: head = [1,2,3,4,5,6]
# Output: [4,5,6]
# Explanation: Since the list has two middle nodes with values 3 and 4, we return the second one.
 

# Constraints:

# The number of nodes in the list is in the range [1, 100].
# 1 <= Node.val <= 100

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val  # Value of the current node.
        self.next = next  # Pointer to the next node in the list.

from typing import Optional

class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
        Finds the middle node of a singly linked list.

        Args:
            head: The head of the linked list (the first node).

        Returns:
            The middle node of the linked list.  If there are two middle nodes,
            returns the second one.
        """
        slow = head  # Initialize a 'slow' pointer to the head of the list.
        fast = head  # Initialize a 'fast' pointer to the head of the list.

        # Iterate until the 'fast' pointer reaches the end of the list (or None).
        while fast and fast.next:
            # The 'fast' pointer moves two nodes at a time.
            fast = fast.next.next
            # The 'slow' pointer moves one node at a time.
            slow = slow.next

        # When the 'fast' pointer reaches the end, the 'slow' pointer will be at the middle.
        return slow
            
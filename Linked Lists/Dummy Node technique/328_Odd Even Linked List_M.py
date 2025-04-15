# Given the head of a singly linked list, group all the nodes with odd indices together followed by the nodes with even indices, and return the reordered list.

# The first node is considered odd, and the second node is even, and so on.

# Note that the relative order inside both the even and odd groups should remain as it was in the input.

# You must solve the problem in O(1) extra space complexity and O(n) time complexity.

 

# Example 1:


# Input: head = [1,2,3,4,5]
# Output: [1,3,5,2,4]
# Example 2:


# Input: head = [2,1,3,5,6,4,7]
# Output: [2,3,6,7,1,5,4]
 

# Constraints:

# The number of nodes in the linked list is in the range [0, 104].
# -106 <= Node.val <= 106

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        oddlist_head = ListNode(0)
        oddlist_tail = oddlist_head
        
        evenlist_head = ListNode(0)
        evenlist_tail = evenlist_head
        
        i = 1
        while head:
            if i % 2 == 0:
                evenlist_tail.next = ListNode(head.val)
                evenlist_tail = evenlist_tail.next
            
            else:
                oddlist_tail.next = ListNode(head.val)
                oddlist_tail = oddlist_tail.next
            
            head = head.next
            i += 1
        
        oddlist_tail.next = evenlist_head.next
        
        return oddlist_head.next
        
# a better solution
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
        Given the head of a singly linked list, group all the nodes with odd indices together followed by the nodes with even indices, and return the reordered list.

        The first node is considered odd, and the second node is considered even, and so on.

        The relative order inside both the even and odd groups should remain as it was in the input.

        You must solve the problem in O(1) extra space complexity.

        Args:
            head: The head of the singly linked list.

        Returns:
            The head of the reordered linked list.
        """

        # Handle edge cases: empty list or list with only one node.
        if not head or not head.next:
            return head

        # Initialize pointers:
        # 'odd' points to the current odd node.
        odd = head
        # 'even' points to the current even node.
        even = head.next
        # 'even_start' stores the head of the even list, which is needed to connect it to the end of the odd list.
        even_start = even

        # Iterate through the list, rearranging the nodes.
        while even and even.next:
            # Connect the current odd node to the next odd node (skipping the even node).
            odd.next = even.next
            # Move the 'odd' pointer to the next odd node.
            odd = odd.next
            # Connect the current even node to the next even node (skipping the odd node).
            even.next = odd.next
            # Move the 'even' pointer to the next even node.
            even = even.next

        # Connect the tail of the odd list to the head of the even list.
        odd.next = even_start
        # Return the head of the modified list (which is still the original head).
        return head   
        
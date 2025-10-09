# You are given the head of a singly linked-list. The list can be represented as:

# L0 → L1 → … → Ln - 1 → Ln
# Reorder the list to be on the following form:

# L0 → Ln → L1 → Ln - 1 → L2 → Ln - 2 → …
# You may not modify the values in the list's nodes. Only nodes themselves may be changed.

 

# Example 1:


# Input: head = [1,2,3,4]
# Output: [1,4,2,3]
# Example 2:


# Input: head = [1,2,3,4,5]
# Output: [1,5,2,4,3]
 

# Constraints:

# The number of nodes in the list is in the range [1, 5 * 104].
# 1 <= Node.val <= 1000

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        def two_pointer(head):
            left, right = head, head
            right_pre = None
            count = 1
            while right.next:
                right_pre = right
                right = right.next
                count += 1
            
            if count <= 2:
                return
            
            else:
                right.next = left.next
                left.next = right
                right_pre.next = None
            
            two_pointer(right.next)
        
        two_pointer(head)
        
# a better one avoid repeatedly traverses
# Time: O(n)
# Space: O(1)
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Reorders the list in O(N) time and O(1) space.
        Do not return anything, modify head in-place instead.
        """
        if not head or not head.next:
            return

        # Step 1: Find the middle of the list
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        # At this point, 'slow' is the head of the second half
        second_half = slow.next
        # Split the list into two halves
        slow.next = None

        # Step 2: Reverse the second half
        prev = None
        curr = second_half
        while curr:
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node
        # 'prev' is now the head of the reversed second half
        second_half_reversed = prev

        # Step 3: Merge the two halves
        first_half = head
        while second_half_reversed:
            # Save the next nodes
            temp1 = first_half.next
            temp2 = second_half_reversed.next
            
            # Interleave
            first_half.next = second_half_reversed
            second_half_reversed.next = temp1
            
            # Move pointers forward
            first_half = temp1
            second_half_reversed = temp2
        
        
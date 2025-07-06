# Given the head of a linked list, rotate the list to the right by k places.

 

# Example 1:


# Input: head = [1,2,3,4,5], k = 2
# Output: [4,5,1,2,3]
# Example 2:


# Input: head = [0,1,2], k = 4
# Output: [2,0,1]
 

# Constraints:

# The number of nodes in the list is in the range [0, 500].
# -100 <= Node.val <= 100
# 0 <= k <= 2 * 109

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
  def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
    
    # Handle edge cases: no rotation needed for empty or single-node lists.
    if not head or not head.next:
      return head
    
    # Initialize two pointers, 'slow' and 'fast', at the head.
    slow = head
    fast = head

    # Create a gap of 'k' nodes between 'slow' and 'fast'.
    # This section also handles cases where 'k' is larger than the list's length.
    for i in range(k):
      if fast.next:
        fast = fast.next
      else:
        # If 'k' >= length, calculate the list length 'n'.
        n = i + 1
        # Find the effective rotation amount.
        k_reminder = k % n
        # Reset 'fast' and move it by the effective amount.
        fast = head
        for _ in range(k_reminder):
          fast = fast.next
        # Exit the loop since the gap is now correct.
        break
    
    # Move both pointers until 'fast' reaches the last node.
    # 'slow' will then be pointing to the new tail of the list.
    while fast.next:
      fast = fast.next
      slow = slow.next
    
    # Perform the rotation.
    fast.next = head      # Connect the old tail to the old head, creating a circle.
    res = slow.next       # The new head is the node after 'slow'.
    slow.next = None      # Break the circle at the new tail.
    
    return res


class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        
        if not head or not head.next:
            return head
        
        slow = head
        fast = head

        for i in range(k):
            if fast.next:
                fast = fast.next
            else:
                fast = head
                n = i + 1
                k_reminder = k % n
                for j in range(k_reminder):
                    fast = fast.next
                break
        
        while fast.next:
            fast = fast.next
            slow = slow.next
        
        fast.next = head
        res = slow.next
        slow.next = None
        
        return res
        
            
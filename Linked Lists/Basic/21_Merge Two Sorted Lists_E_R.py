# You are given the heads of two sorted linked lists list1 and list2.

# Merge the two lists into one sorted list. The list should be made by splicing together the nodes of the first two lists.

# Return the head of the merged linked list.

 

# Example 1:


# Input: list1 = [1,2,4], list2 = [1,3,4]
# Output: [1,1,2,3,4,4]
# Example 2:

# Input: list1 = [], list2 = []
# Output: []
# Example 3:

# Input: list1 = [], list2 = [0]
# Output: [0]
 

# Constraints:

# The number of nodes in both lists is in the range [0, 50].
# -100 <= Node.val <= 100
# Both list1 and list2 are sorted in non-decreasing order.


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val  # Store the value of the node
        self.next = next  # Pointer to the next node in the list

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()  # Create a dummy node to simplify the merging process
        curr = dummy  # Initialize a 'curr' pointer to the dummy node

        while list1 and list2:  # Iterate while both lists have nodes
            if list1.val >= list2.val:  # Compare values of current nodes in both lists
                curr.next = list2  # Add the smaller node (list2) to the merged list
                list2 = list2.next  # Move the list2 pointer to the next node
            else:
                curr.next = list1  # Add the smaller node (list1) to the merged list
                list1 = list1.next  # Move the list1 pointer to the next node
            curr = curr.next  # Move the 'curr' pointer to the newly added node

        curr.next = list1 if list1 else list2  # Append the remaining nodes from either list1 or list2
        return dummy.next  # Return the next node after the dummy node (the actual merged list)
# You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.

# You may assume the two numbers do not contain any leading zero, except the number 0 itself.

 

# Example 1:


# Input: l1 = [2,4,3], l2 = [5,6,4]
# Output: [7,0,8]
# Explanation: 342 + 465 = 807.
# Example 2:

# Input: l1 = [0], l2 = [0]
# Output: [0]
# Example 3:

# Input: l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
# Output: [8,9,9,9,0,0,0,1]
 

# Constraints:

# The number of nodes in each linked list is in the range [1, 100].
# 0 <= Node.val <= 9
# It is guaranteed that the list represents a number that does not have leading zeros.

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        num1 = ''
        num2 = ''
        
        curr1 = l1
        curr2 = l2
        
        while curr1 or curr2:
            if curr1:
                num1 += str(curr1.val)
                curr1 = curr1.next
                
            if curr2:
                num2 += str(curr2.val)
                curr2 = curr2.next
            
        sum_ = int(num1[::-1]) + int(num2[::-1])
        sum_ = str(sum_)[::-1]
        
        res = ListNode(int(sum_[0]))  # Initialize res with the first digit
        curr = res
        for i in range(1, len(sum_)):
            curr.next = ListNode(int(sum_[i]))  # Set value *during* node creation
            curr = curr.next
        return res


# A better solution:
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        dummy = ListNode()
        res = dummy
        
        cur1 = l1
        cur2 = l2
        
        carry = 0
        
        while cur1 or cur2 or carry:
            cur_sum = carry
            
            if cur1:
                cur_sum += cur1.val
                cur1 = cur1.next
                
            if cur2:
                cur_sum += cur2.val
                cur2 = cur2.next
            
            num = cur_sum % 10
            carry = cur_sum // 10
            
            dummy.next = ListNode(num)
            dummy = dummy.next
        return res.next
            
                
            
            
            
            
            
        
        
            
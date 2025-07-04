# Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

# An input string is valid if:

# Open brackets must be closed by the same type of brackets.
# Open brackets must be closed in the correct order.
# Every close bracket has a corresponding open bracket of the same type.
 

# Example 1:

# Input: s = "()"

# Output: true

# Example 2:

# Input: s = "()[]{}"

# Output: true

# Example 3:

# Input: s = "(]"

# Output: false

# Example 4:

# Input: s = "([])"

# Output: true

 

# Constraints:

# 1 <= s.length <= 104
# s consists of parentheses only '()[]{}'.

class Solution:
    
    def isValid(self, s: str) -> bool:
        
        stack =  []
        mapping = {")": "(", "]": "[", "}": "{"}
        for char in s:
            if char in mapping:
                if not stack or stack.pop() != mapping[char]:
                    return False 
            else:
                stack.append(char)

        return not stack 

             
class Solution:
    """
    This class provides a solution to determine if a string containing 
    parentheses is valid.
    """
    def isValid(self, s: str) -> bool:
        
        stack = [] # Initialize a stack to store open brackets
        mapping = {")": "(", "]": "[", "}": "{"} # Mapping of closing brackets to their corresponding opening brackets
        
        for char in s:
            if char in mapping:
                if not stack or stack.pop() != mapping[char]:
                    return False
            else:
                stack.append(char)
        
        return not stack 
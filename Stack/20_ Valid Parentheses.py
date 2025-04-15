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
    """
    This class provides a solution to determine if a string containing 
    parentheses is valid.
    """
    def isValid(self, s: str) -> bool:
        """
        Determines if the input string containing only the characters '(', ')', '{', '}', '[' and ']' is valid.

        An input string is valid if:
            - Open brackets must be closed by the same type of brackets.
            - Open brackets must be closed in the correct order.
            - Every close bracket has a corresponding open bracket of the same type.

        Args:
            s (str): The input string containing parentheses.

        Returns: 
            bool: True if the string is valid, False otherwise.
        """
        stack =  []# Initialize a stack to store open brackets
        mapping = {")": "(", "]": "[", "}": "{"}  # Mapping of closing brackets to their corresponding opening brackets

        for char in s:  # Iterate through each character in the string
            if char in mapping:  # If the character is a closing bracket
                if not stack or stack.pop() != mapping[char]:  # Check if the stack is empty or the top element doesn't match the expected opening bracket
                    return False  # If not, the string is invalid
            else:
                stack.append(char)  # If the character is an opening bracket, push it onto the stack

        return not stack  # If the stack is empty at the end, all brackets were closed correctly, so return True; otherwise, return False
                
            
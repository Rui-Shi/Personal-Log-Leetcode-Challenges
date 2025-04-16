# You are given an array of strings tokens that represents an arithmetic expression in a Reverse Polish Notation.

# Evaluate the expression. Return an integer that represents the value of the expression.

# Note that:

# The valid operators are '+', '-', '*', and '/'.
# Each operand may be an integer or another expression.
# The division between two integers always truncates toward zero.
# There will not be any division by zero.
# The input represents a valid arithmetic expression in a reverse polish notation.
# The answer and all the intermediate calculations can be represented in a 32-bit integer.
 

# Example 1:

# Input: tokens = ["2","1","+","3","*"]
# Output: 9
# Explanation: ((2 + 1) * 3) = 9
# Example 2:

# Input: tokens = ["4","13","5","/","+"]
# Output: 6
# Explanation: (4 + (13 / 5)) = 6
# Example 3:

# Input: tokens = ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]
# Output: 22
# Explanation: ((10 * (6 / ((9 + 3) * -11))) + 17) + 5
# = ((10 * (6 / (12 * -11))) + 17) + 5
# = ((10 * (6 / -132)) + 17) + 5
# = ((10 * 0) + 17) + 5
# = (0 + 17) + 5
# = 17 + 5
# = 22

from typing import List


class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        def is_integer_string(s):
            try:
                int(s)
                return True
            except:
                return False
        
                
        stack = []
        
        for item in tokens:
            if is_integer_string(item):
                stack.append(int(item))
            else:
                a = stack.pop()
                b = stack.pop()
                
                if item == "/":
                    stack.append(int(b / a))
                elif item == "*":
                    stack.append(a * b)
                elif item == "+":
                    stack.append(a + b)
                else:
                    stack.append(b - a)
            
        return stack[-1]
    
s = Solution()
test1 = ["2","1","+","3","*"]
test2 = ["4","13","5","/","+"]
print(s.evalRPN(test1))
print(s.evalRPN(test2))

        
# Given two binary strings a and b, return their sum as a binary string.

 

# Example 1:

# Input: a = "11", b = "1"
# Output: "100"
# Example 2:

# Input: a = "1010", b = "1011"
# Output: "10101"
 

# Constraints:

# 1 <= a.length, b.length <= 104
# a and b consist only of '0' or '1' characters.
# Each string does not contain leading zeros except for the zero itself.



class Solution:
    def addBinary(self, a: str, b: str) -> str:
        """
        Adds two binary strings represented as strings.

        Args:
            a: The first binary string.
            b: The second binary string.

        Returns:
            The sum of the two binary strings as a string.

        Time Complexity: O(max(m, n)), where m is the length of 'a' and n is the length of 'b'.
        Space Complexity: O(max(m, n)), due to the space used by the 'result' string.  In the worst case, the result string can have a length equal to the sum of the lengths of the input strings.
        """
        i = len(a) - 1  # Initialize index for string 'a' (from right to left)
        j = len(b) - 1  # Initialize index for string 'b' (from right to left)
        carry = 0       # Initialize carry to 0
        result = ""    # Initialize the result string

        while i >= 0 or j >= 0 or carry:  # Continue as long as there are bits left to process in either string or a carry exists
            bit_a = int(a[i]) if i >= 0 else 0  # Get the current bit from 'a', or 0 if index is out of bounds
            bit_b = int(b[j]) if j >= 0 else 0  # Get the current bit from 'b', or 0 if index is out of bounds

            current_sum = bit_a + bit_b + carry  # Calculate the sum of the current bits and the carry
            result = str(current_sum % 2) + result  # Add the least significant bit of the sum to the beginning of the result string
            carry = current_sum // 2  # Calculate the new carry (integer division by 2)

            i -= 1  # Decrement the index for string 'a'
            j -= 1  # Decrement the index for string 'b'

        return result  # Return the final result string
#### Strings in Python are immutable; you can't change individual characters in place. You have to create new strings.

class Solution:
    def addBinary(self, a: str, b: str) -> str:
        i = len(a) - 1
        j = len(b) - 1
        carry = 0
        result = ""
        
        while i >= 0 or j >= 0 or carry:
            bit_a = int(a[i]) if i >= 0 else 0
            bit_b = int(b[i]) if i >= 0 else 0
            
            current_sum = bit_a + bit_b + carry
            result += str(current_sum % 2) + result
            carry = current_sum // 2
            i -= 1
            j -= 1
        return result
              
            

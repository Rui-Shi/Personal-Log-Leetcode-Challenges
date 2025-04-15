# Given an integer x, return true if x is a 
# palindrome
# , and false otherwise.

 

# Example 1:

# Input: x = 121
# Output: true
# Explanation: 121 reads as 121 from left to right and from right to left.
# Example 2:

# Input: x = -121
# Output: false
# Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.
# Example 3:

# Input: x = 10
# Output: false
# Explanation: Reads 01 from right to left. Therefore it is not a palindrome.

class Solution:
    def isPalindrome(self, x: int) -> bool:
        digits_list = [str(digit) for digit in str(x)] # convert a number into a list of single digit (str)
        if digits_list[::-1] == digits_list:
            return True
        else:
            return False

# solusion 2
def number_to_digit_list(number):
  """Converts a number to a list of strings, each representing a digit.

  Args:
    number: The number to convert (can be int or float).

  Returns:
    A list of strings.
  """
  return list(map(str, str(number))) 
# the map function applies the str function to each in the list

# Example Usage
number = 12345
digit_list = number_to_digit_list(number)
print(digit_list)  # Output: ['1', '2', '3', '4', '5']
# A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.

# Given a string s, return true if it is a palindrome, or false otherwise.

 

# Example 1:

# Input: s = "A man, a plan, a canal: Panama"
# Output: true
# Explanation: "amanaplanacanalpanama" is a palindrome.
# Example 2:

# Input: s = "race a car"
# Output: false
# Explanation: "raceacar" is not a palindrome.
# Example 3:

# Input: s = " "
# Output: true
# Explanation: s is an empty string "" after removing non-alphanumeric characters.
# Since an empty string reads the same forward and backward, it is a palindrome.
 

# Constraints:

# 1 <= s.length <= 2 * 105
# s consists only of printable ASCII characters.

class Solution:
    def isPalindrome(self, s: str) -> bool:
        s_clean = ""
        
        s = s.lower()

        for char in s:
            if char.isalnum(): # check if a char is a letter or num
                s_clean += char
                
        if s_clean == s_clean[::-1]:
            return True
        
        else:
            return False

# Time: O(n)
# Space: O(n) it create a new string O(n)
class Solution:
    def isPalindrome(self, s: str) -> bool:
        s_clean = ""
        
        s = s.lower() # change all to the lower case: O(n)
        
        for char in s: # O(n)
            if char.isalnum():
                s_clean += char
        
        if s_clean == s_clean[::-1]:
            return True
        
        else:
            return False


        
        
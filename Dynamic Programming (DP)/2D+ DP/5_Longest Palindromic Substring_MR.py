# Given a string s, return the longest palindromic substring in s.

 

# Example 1:

# Input: s = "babad"
# Output: "bab"
# Explanation: "aba" is also a valid answer.
# Example 2:

# Input: s = "cbbd"
# Output: "bb"
 

# Constraints:

# 1 <= s.length <= 1000
# s consist of only digits and English letters.

class Solution:
  def _expand_around_center(self, s: str, n: int, left: int, right: int):
    """
    Helper function to expand around the center defined by `left` and `right` indices.
    It updates `self.res_start` and `self.res_len` if a longer palindrome is found.

    Args:
      s: The input string.
      n: The length of the string `s`.
      left: The initial left pointer for the center.
      right: The initial right pointer for the center.
             For odd length palindromes, left == right.
             For even length palindromes, right == left + 1.
    """
    # Loop as long as pointers are within bounds and characters at pointers match
    while left >= 0 and right < n and s[left] == s[right]:
      current_len = right - left + 1
      # If this palindrome is longer than the current longest found
      if current_len > self.res_len:
        self.res_len = current_len
        self.res_start = left  # Store the start of this new longest palindrome
      
      # Expand outwards from the center
      left -= 1
      right += 1

  def longestPalindrome(self, s: str) -> str:
    """
    Given a string s, return the longest palindromic substring in s.
    """
    n = len(s)

    # Constraints: 1 <= s.length <= 1000.
    # So, s is never empty.
    # If s has only one character, it's its own longest palindrome.
    if n < 2:
      return s

    # Initialize attributes to store the start index and length of the longest palindrome.
    # We default to the first character being a palindrome of length 1.
    # This ensures that if no palindrome longer than 1 character exists,
    # a single character (which is a palindrome) is returned.
    self.res_start = 0
    self.res_len = 1

    # Iterate through each character of the string.
    # Each character s[i] can be the center of an odd-length palindrome.
    # Each pair s[i], s[i+1] can be the center of an even-length palindrome.
    for i in range(n):
      # Check for odd length palindromes (center is s[i])
      # Example: For "aba", if i points to 'b', center is (i, i).
      self._expand_around_center(s, n, i, i)
      
      # Check for even length palindromes (center is between s[i] and s[i+1])
      # Example: For "abba", if i points to the first 'b', center is (i, i+1).
      # The helper's `while` loop condition `right < n` correctly handles the edge case
      # when `i` is `n-1`, so `i+1` would be `n` (out of bounds for initial `s[right]`).
      self._expand_around_center(s, n, i, i + 1)
            
    # After checking all possible centers, extract the longest palindrome found.
    return s[self.res_start : self.res_start + self.res_len]

class Solution:
    def longestPalindrome(self, s: str) -> str:

        self.res_left = 0
        self.res_right = 0
        self.max_len = 0

        def expand_palindromic(s, left, right):
            n = len(s)
            while left >= 0 and right < n and s[left] == s[right]:
                if right - left > self.max_len:
                    self.res_left, self.res_right = left, right
                    self.max_len = right - left
                left -= 1
                right += 1

        for i in range(len(s)):
            expand_palindromic(s, i, i)
            expand_palindromic(s, i, i + 1)
        
        return s[self.res_left : self.res_right + 1]
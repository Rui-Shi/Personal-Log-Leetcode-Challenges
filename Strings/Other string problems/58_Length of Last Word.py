# Given a string s consisting of words and spaces, return the length of the last word in the string.

# A word is a maximal 
# substring
#  consisting of non-space characters only.

 

# Example 1:

# Input: s = "Hello World"
# Output: 5
# Explanation: The last word is "World" with length 5.
# Example 2:

# Input: s = "   fly me   to   the moon  "
# Output: 4
# Explanation: The last word is "moon" with length 4.
# Example 3:

# Input: s = "luffy is still joyboy"
# Output: 6
# Explanation: The last word is "joyboy" with length 6.

class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        """
        Calculates the length of the last word in a string.

        Args:
            s: The input string.

        Returns:
            The length of the last word in the string.  Returns 0 if no word is found.
        """

        s_inverse = s[::-1]  # Reverse the string for easier traversal from the end

        i = 0  # Initialize a pointer 'i' to traverse the reversed string
        k = 0  # Initialize a counter 'k' to store the length of the last word

        # Skip trailing non-alphanumeric characters (spaces, punctuation, etc.)
        while i < len(s) and not s_inverse[i].isalnum(): 
            i += 1  # Move the pointer forward

        # Count the length of the last word (alphanumeric characters)
        while i < len(s) and s_inverse[i].isalnum():
            k += 1  # Increment the length counter
            i += 1  # Move the pointer forward

        return k  # Return the length of the last word

s = Solution()
print(s.lengthOfLastWord("Hello World   "))


class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        s_inverse = s[::-1]
        
        i = 0
        count = 0
        s_inverse = s_inverse.lstrip()
        
        while i <= len(s_inverse):
            if s_inverse[i].isalpha():
                count += 1
                i += 1
            
            else:
                break
        
        return count
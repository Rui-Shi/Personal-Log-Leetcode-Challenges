# Given a string s, reverse only all the vowels in the string and return it.

# The vowels are 'a', 'e', 'i', 'o', and 'u', and they can appear in both lower and upper cases, more than once.

 

# Example 1:

# Input: s = "IceCreAm"

# Output: "AceCreIm"

# Explanation:

# The vowels in s are ['I', 'e', 'e', 'A']. On reversing the vowels, s becomes "AceCreIm".

# Example 2:

# Input: s = "leetcode"

# Output: "leotcede"

class Solution(object):
    def reverseVowels(self, s):
        # Convert the input string to a character array.
        word = list(s)
        left = 0
        right = len(s) - 1
        vowels = "aeiouAEIOU"
        
        while left < right:
            while left < right and word[left] not in vowels:
                left += 1
            while left < right and word[right] not in vowels:
                right -= 1
            if left < right:
                word[left], word[right] = word[right], word[left]
                left += 1
                right -= 1
        
        return ''.join(word)
            
            
        
        
            
            
                
            
        
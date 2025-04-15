# Given two strings s and t, return true if t is an 
# anagram
#  of s, and false otherwise.

 

# Example 1:

# Input: s = "anagram", t = "nagaram"

# Output: true

# Example 2:

# Input: s = "rat", t = "car"

# Output: false

 

# Constraints:

# 1 <= s.length, t.length <= 5 * 104
# s and t consist of lowercase English letters.

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        """
        Checks if two strings are anagrams of each other.

        Args:
            s: The first string.
            t: The second string.

        Returns:
            True if the strings are anagrams, False otherwise.
        """

        # If the lengths of the strings are different, they cannot be anagrams.
        if len(s) != len(t):
            return False

        # Create dictionaries to store the frequency of each character in both strings.
        s_dict = {}  # Dictionary for string 's'
        t_dict = {}  # Dictionary for string 't'

        # Iterate through the first string 's' and count character frequencies.
        for letter in s:
            if letter not in s_dict:
                s_dict[letter] = 1  # Initialize count if character is seen for the first time
            else:
                s_dict[letter] += 1  # Increment count if character is already in the dictionary

        # Iterate through the second string 't' and count character frequencies.
        for letter in t:
            if letter not in t_dict:
                t_dict[letter] = 1  # Initialize count
            else:
                t_dict[letter] += 1  # Increment count

        # If the number of unique characters is different, they cannot be anagrams.
        if len(s_dict) != len(t_dict):
            return False

        # Iterate through the character counts in the dictionary for string 's'.
        for key, value in s_dict.items():
            # Check if the character exists in the dictionary for string 't'.
            if key not in t_dict:
                return False  # If a character is in 's' but not in 't', they are not anagrams.
            else:
                # Check if the frequencies of the character are the same in both strings.
                if value != t_dict[key]:
                    return False  # If the frequencies don't match, they are not anagrams.

        return True  # If all checks pass, the strings are anagrams.
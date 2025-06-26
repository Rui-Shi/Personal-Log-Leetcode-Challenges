# Given a pattern and a string s, find if s follows the same pattern.

# Here follow means a full match, such that there is a bijection between a letter in pattern and a non-empty word in s. Specifically:

# Each letter in pattern maps to exactly one unique word in s.
# Each unique word in s maps to exactly one letter in pattern.
# No two letters map to the same word, and no two words map to the same letter.
 

# Example 1:

# Input: pattern = "abba", s = "dog cat cat dog"

# Output: true

# Explanation:

# The bijection can be established as:

# 'a' maps to "dog".
# 'b' maps to "cat".
# Example 2:

# Input: pattern = "abba", s = "dog cat cat fish"

# Output: false

# Example 3:

# Input: pattern = "aaaa", s = "dog cat cat dog"

# Output: false

class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        mapping = {}
        s_words = s.split() # It finds these whitespace characters (default) and splits the string at those points
        if len(pattern) != len(s_words):
            return False
        for i, word in enumerate(s_words):
            if word not in mapping:
                if pattern[i] not in mapping.values():
                    mapping[word] = pattern[i]
                else:
                    return False
            else:
                if mapping[word] != pattern[i]:
                    return False
        return True
    
class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        s_words = s.split()
        mapping = {}
        
        if len(pattern) != len(s_words):
            return False
        
        for i, char in enumerate(pattern):
            if char in mapping:
                if mapping[char] != s_words[i]:
                    return False
                
            elif s_words[i] in mapping.values():
                return False
            
            else:
                mapping[char] = s_words[i]
        
        return True
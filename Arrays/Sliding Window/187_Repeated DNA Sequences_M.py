# The DNA sequence is composed of a series of nucleotides abbreviated as 'A', 'C', 'G', and 'T'.

# For example, "ACGAATTCCG" is a DNA sequence.
# When studying DNA, it is useful to identify repeated sequences within the DNA.

# Given a string s that represents a DNA sequence, return all the 10-letter-long sequences (substrings) that occur more than once in a DNA molecule. You may return the answer in any order.

 

# Example 1:

# Input: s = "AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT"
# Output: ["AAAAACCCCC","CCCCCAAAAA"]
# Example 2:

# Input: s = "AAAAAAAAAAAAA"
# Output: ["AAAAAAAAAA"]

import collections
class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        freq_map = collections.defaultdict(int)
        left = 0
        right = left + 10
        res = []
        # edge case: when len(s) <= 10
        if len(s) <= 10:
            return res
        
        while right <= len(s):
            str = s[left : right]
            freq_map[str] += 1
            if freq_map[str] == 2:
                res.append(str)
            left += 1
            right = left + 10
        
        return res
        
        
        
        
 
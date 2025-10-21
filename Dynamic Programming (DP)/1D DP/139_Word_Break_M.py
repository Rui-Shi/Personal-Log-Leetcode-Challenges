# Given a string s and a dictionary of strings wordDict, return true if s can be segmented into 
# a space-separated sequence of one or more dictionary words.

# Note that the same word in the dictionary may be reused multiple times in the segmentation.

 

# Example 1:

# Input: s = "leetcode", wordDict = ["leet","code"]
# Output: true
# Explanation: Return true because "leetcode" can be segmented as "leet code".
# Example 2:

# Input: s = "applepenapple", wordDict = ["apple","pen"]
# Output: true
# Explanation: Return true because "applepenapple" can be segmented as "apple pen apple".
# Note that you are allowed to reuse a dictionary word.
# Example 3:

# Input: s = "catsandog", wordDict = ["cats","dog","sand","and","cat"]
# Output: false
 

# Constraints:

# 1 <= s.length <= 300
# 1 <= wordDict.length <= 1000
# 1 <= wordDict[i].length <= 20
# s and wordDict[i] consist of only lowercase English letters.
# All the strings of wordDict are unique.

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        """
        Determines if a string 's' can be segmented into a space-separated sequence
        of one or more dictionary words.

        Args:
            s: The input string to be segmented.
            wordDict: A list of words that can be used for segmentation.

        Returns:
            True if 's' can be segmented, False otherwise.
        """

        # dp[i] will be True if the substring s[0...i-1] can be segmented
        # dp[0] is True as an empty string can always be segmented (base case)
        dp = [True] + [False] * len(s)

        # Iterate through all possible end positions (i) in the string 's'
        # 'i' represents the length of the current prefix s[0...i-1]
        for i in range(1, len(s) + 1):
            # For each prefix, iterate through every word in the dictionary
            for w in wordDict:  
                # Calculate the potential starting index for the current word 'w'
                # If s[start:i] matches 'w', then the prefix s[0...i-1] is formed
                # by s[0...start-1] followed by 'w'.
                start = i - len(w)

                # Check three conditions:
                # 1. 'start' is a valid index (not negative)
                # 2. The prefix s[0...start-1] (represented by dp[start]) is already segmentable
                # 3. The current substring s[start:i] exactly matches the dictionary word 'w'
                if start >= 0 and dp[start] and s[start:i] == w:
                    # If all conditions are met, it means s[0...i-1] can be segmented.
                    dp[i] = True
                    # Once a valid segmentation is found for s[0...i-1], no need to check other words
                    break

        # The final result is stored in dp[len(s)], which indicates whether
        # the entire string 's' (s[0...len(s)-1]) can be segmented.
        return dp[-1]


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dp = [True] + [False] * len(s)
        for i in range(1, len(s) + 1):
            for word in wordDict:
                n = len(word)
                start = i - n
                if start > 0 and dp[start] and s[start:i] == word:
                    dp[i] = True
        
        return dp[-1]

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dp = [True] + [False] * len(s)
        
        for i in range(1, len(s) + 1):
            for word in wordDict:
                start = i - len(word)
                if start >= 0 and dp[start] == True and s[start:i] == word:
                    dp[i] = True
                    break
        
        return dp[-1]
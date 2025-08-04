# Given an array of strings strs, group the 
# anagrams
#  together. You can return the answer in any order.

 

# Example 1:

# Input: strs = ["eat","tea","tan","ate","nat","bat"]

# Output: [["bat"],["nat","tan"],["ate","eat","tea"]]

# Explanation:

# There is no string in strs that can be rearranged to form "bat".
# The strings "nat" and "tan" are anagrams as they can be rearranged to form each other.
# The strings "ate", "eat", and "tea" are anagrams as they can be rearranged to form each other.
# Example 2:

# Input: strs = [""]

# Output: [[""]]

# Example 3:

# Input: strs = ["a"]

# Output: [["a"]]

# My solution:
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        """
        Groups anagrams together from a list of strings.

        Args:
            strs: A list of strings.

        Returns:
            A list of lists, where each inner list contains anagrams.
        """

        # Create a dictionary to store the anagrams.
        # The keys will be the sorted versions of the strings (used as identifiers for anagram groups).
        # The values will be lists of the original strings that are anagrams of each other.
        anagrams = {}

        # Iterate through the input list of strings.
        for str in strs:
            # Sort the characters of the current string alphabetically.
            # This sorted string will be the key in the 'anagrams' dictionary.
            # "separator".join(iterable), separator is the string that will be placed between the elements.
            # iterable is the sequence of strings you want to join.
            str_sorted = ''.join(sorted(str))

            # Check if a group of anagrams with this sorted string already exists in the dictionary.
            if str_sorted in anagrams:
                # If it exists, append the current string to the existing group.
                anagrams[str_sorted].append(str)
            else:
                # If it doesn't exist, create a new group with the sorted string as the key
                # and a list containing the current string as the first element.
                anagrams[str_sorted] = [str]

        # Return the values of the dictionary, which are the lists of anagrams.
        # We convert the dictionary's values (which are a collection of lists) to a list of lists.
        return list(anagrams.values())
            
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        map = {}
        for str in strs:
            str_sorted = ''.sorted(str)
            
            if str_sorted in map:
                map[str_sorted].append(str)
            
            else:
                map[str_sorted] = [str]
        
        return list(map.values()) # output the value of dict and convert it to list.
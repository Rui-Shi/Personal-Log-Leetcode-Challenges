# Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could represent. Return the answer in any order.

# A mapping of digits to letters (just like on the telephone buttons) is given below. Note that 1 does not map to any letters.


 

# Example 1:

# Input: digits = "23"
# Output: ["ad","ae","af","bd","be","bf","cd","ce","cf"]
# Example 2:

# Input: digits = ""
# Output: []
# Example 3:

# Input: digits = "2"
# Output: ["a","b","c"]
 

# Constraints:

# 0 <= digits.length <= 4
# digits[i] is a digit in the range ['2', '9'].

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        n = len(digits)
        
        if n == 0:
            return []
        
        maps = {'2': 'abc',
                '3': 'def',
                '4': 'ghi',
                '5': 'jkl',
                '6': 'mno',
                '7': 'pqrs',
                '8': 'tuv',
                '9': 'wxyz'}
        
        res = ['']
        
        for digit in digits:
            res_next = []
            letters = maps[digit]
            for str in res:
                for char in letters:
                    res_next.append(str + char)
            res[:] = res_next
        
        return res_next

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        n = len(digits)
        
        if n == 0:
            return []
        
        maps = {'2': 'abc',
                '3': 'def',
                '4': 'ghi',
                '5': 'jkl',
                '6': 'mno',
                '7': 'pqrs',
                '8': 'tuv',
                '9': 'wxyz'}
        
        res = ['']
        
        for digit in digits:
            res_next = []
            letters = maps[digit]
            for str in res:
                for char in letters:
                    res_next.append(str + char)
            res[:] = res_next
        
        return res     

# use backtrack                 
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        map = {
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz'
        }
        res = []
        def backtrack_helper(cur_comb):
            if len(cur_comb) == len(digits):
                res.append(cur_comb)
            
            else:
                candidates = map[digits[len(cur_comb)]]
                for candidate in candidates:
                    backtrack_helper(cur_comb + candidate)
        
        backtrack_helper('')
        
        return res

# Time complexity:
# Let N be the length of the input digits string.
# Time: O(N * 4^N) depth: N, combinations: 4^N
# Auxiliary space: O(N)
# Total Space with result: O(N*4N)
          
              
                
                
            
            
                
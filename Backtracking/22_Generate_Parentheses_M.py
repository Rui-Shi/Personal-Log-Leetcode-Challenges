# Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

 

# Example 1:

# Input: n = 3
# Output: ["((()))","(()())","(())()","()(())","()()()"]
# Example 2:

# Input: n = 1
# Output: ["()"]
 

# Constraints:

# 1 <= n <= 8

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = set()
        
        def backtrack_helper(cur_comb, left_count, right_count, n):
            if len(cur_comb) == 2 * n:
                res.add(cur_comb)
                return
            
            elif left_count > right_count:
                if left_count < n:
                    backtrack_helper(cur_comb + "(", left_count + 1, right_count, n)

                backtrack_helper(cur_comb + ")", left_count, right_count + 1, n)
            
            else:
                backtrack_helper(cur_comb + "(", left_count + 1, right_count, n)
        
        backtrack_helper("", 0, 0, n)
        return list(res)

# Time: O(n * 2^n)
# Space: O(n)
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        
        def backtrack(cur_comb, left_count, right_count, n):
            if len(cur_comb) == 2 * n:
                res.append(cur_comb)
                return
            
            elif left_count > right_count:
                if left_count < n:
                    backtrack(cur_comb + "(", left_count + 1, right_count, n)
                
                backtrack(cur_comb + ")", left_count, right_count + 1, n)
            
            else:
                backtrack(cur_comb + "(", left_count + 1, right_count, n)
            
        backtrack("", 0, 0, n)
        return res
                    
        
        
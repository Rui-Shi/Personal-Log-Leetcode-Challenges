# Write a function such that:

# f(5) outputs
# [5]
# [4,1]
# [3,2]
# [3,1,1]
# [2,2,1]
# [2,1,1,1]
# [1,1,1,1,1]

# f(3) = [
#  [3],
#  [2,1],
#  [1,1,1]
# ]

# Time O(n*2^n): There are 2^(n-1) composition of n (a loose upper bound)
def f(num):
    res = []
    def backtrack_helper(cur_list, start_num, target_num):
        if target_num == 0:
            res.append(cur_list[:])
            return
        
        if target_num < 0:
            return
        
        for i in range(start_num, 0, -1):
            cur_list.append(i)
            backtrack_helper(cur_list, i, target_num - i)
            cur_list.pop()
            
    backtrack_helper([], num, num)
    return res

print(f(5))
print(f(4))
print(f(3))

# Then change the function so that it just outputs the total number of the answers. So in the above case, f(5) outputs 7

# Time: O(n^3):
# Both remaining and threshold can take values 0 to num.
# So the total number of unique subproblems is: O(n^2)
# Each subproblems has up to n loop,
# So the overall complexity is O(n^3)
    
# A corrected function to count integer partitions
def count_partitions(num):
    # dp[r][t] will store partitions of 'r' using parts no larger than 't'
    # Initialize with -1 to indicate 'not yet computed'
    dp = [[-1 for _ in range(num + 1)] for _ in range(num + 1)]

    def h(remaining, threshold, dp):
        # Base case 1: A sum of 0 has exactly one partition (the empty set).
        if remaining == 0:
            return 1
        
        # Base case 2: Invalid if remainder is negative or no parts are allowed.
        if remaining < 0 or threshold == 0:
            return 0

        # Return the stored result if we've already computed this subproblem.
        if dp[remaining][threshold] != -1:
            return dp[remaining][threshold]
        
        res = 0
        for i in range(threshold, 0, -1):
            res += h(remaining - i, min(i, remaining - i), dp)
        
        dp[remaining][threshold] = res
        return res

    return h(num, num, dp)

# Example usage:
print(f"The number of partitions for 7 is: {count_partitions(7)}")
print(f"The number of partitions for 10 is: {count_partitions(10)}")

def count_partitions(num):
    dp = [[-1 for _ in range(num + 1)] for _ in range(num + 1)]
    
    def h(remaining, threshold, dp):
        if remaining == 0:
            dp[remaining][threshold] = 1
            return 1
        
        if remaining < 0 or threshold == 0:
            dp[remaining][threshold] = 0
            return 0
        
        res = 0
        for i in range(threshold, 0, -1):
            res += h(remaining - i, min(i, remaining - i), dp)
        
        dp[remaining][threshold] = res
        return res

    return h(num, num, dp)
            



    
    
    
# You are given an integer array coins representing coins of different denominations and an integer amount representing a total amount of money.

# Return the fewest number of coins that you need to make up that amount. If that amount of money cannot be made up by any combination of the coins, return -1.

# You may assume that you have an infinite number of each kind of coin.

 

# Example 1:

# Input: coins = [1,2,5], amount = 11
# Output: 3
# Explanation: 11 = 5 + 5 + 1
# Example 2:

# Input: coins = [2], amount = 3
# Output: -1
# Example 3:

# Input: coins = [1], amount = 0
# Output: 0
 

# Constraints:

# 1 <= coins.length <= 12
# 1 <= coins[i] <= 231 - 1
# 0 <= amount <= 104

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        coins_set = set(coins)
        
        dp = [0] + [-1] * amount
        
        for i in range(1, amount + 1):
            min_coin = -1
            for coin in coins_set:
                start = i - coin
                
                if start >= 0 and dp[start] >= 0:
                    if min_coin == -1:
                        min_coin = dp[start] + 1
                    else:
                        min_coin = min(min_coin, dp[start] + 1)
            dp[i] = min_coin
        return dp[-1]

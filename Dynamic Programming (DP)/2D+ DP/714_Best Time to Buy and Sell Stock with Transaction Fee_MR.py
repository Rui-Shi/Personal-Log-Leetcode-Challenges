# You are given an array prices where prices[i] is the price of a given stock on the ith day, and an integer fee representing a transaction fee.

# Find the maximum profit you can achieve. You may complete as many transactions as you like, but you need to pay the transaction fee for each transaction.

# Note:

# You may not engage in multiple transactions simultaneously (i.e., you must sell the stock before you buy again).
# The transaction fee is only charged once for each stock purchase and sale.
 

# Example 1:

# Input: prices = [1,3,2,8,4,9], fee = 2
# Output: 8
# Explanation: The maximum profit can be achieved by:
# - Buying at prices[0] = 1
# - Selling at prices[3] = 8
# - Buying at prices[4] = 4
# - Selling at prices[5] = 9
# The total profit is ((8 - 1) - 2) + ((9 - 4) - 2) = 8.
# Example 2:

# Input: prices = [1,3,7,5,10,3], fee = 3
# Output: 6

import math

class Solution:
    def maxProfit(self, prices: list[int], fee: int) -> int:
        """
        Calculates the maximum profit from buying and selling stocks with a transaction fee.

        Args:
            prices: A list of stock prices for consecutive days.
            fee: The transaction fee charged for each buy-sell transaction.

        Returns:
            The maximum achievable profit.
        """
        n = len(prices)
        if n < 2:
            return 0 # Cannot complete a transaction with less than 2 days

        # cash: max profit if we DO NOT hold stock at the end of the day
        # hold: max profit if we DO hold stock at the end of the day

        cash = 0
        hold = -prices[0] # Profit after buying on day 0

        for i in range(1, n):
            prev_cash = cash # Store cash from day i-1 before it's updated

            # Calculate max profit not holding stock today:
            # Option 1: Didn't hold yesterday (cash), don't hold today
            # Option 2: Held yesterday (hold), sell today (prices[i] - fee)
            cash = max(cash, hold + prices[i] - fee)

            # Calculate max profit holding stock today:
            # Option 1: Held yesterday (hold), keep holding today
            # Option 2: Didn't hold yesterday (prev_cash), buy today (-prices[i])
            hold = max(hold, prev_cash - prices[i])

        # Final answer must be in the 'cash' state (profit realized)
        return cash


class Solution:
    def maxProfit(self, prices: list[int], fee: int) -> int:
        n = len(prices)
        
        if n < 2:
            return 0
        
        cash = -prices[0]
        hold = 0
        
        for i in range(1, n):
            hold = max(hold, cash - prices[i] - fee)
            cash = max(cash, hold + prices[i] - fee)
        
        return cash
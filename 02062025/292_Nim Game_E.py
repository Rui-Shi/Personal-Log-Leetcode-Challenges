# You are playing the following Nim Game with your friend:

# Initially, there is a heap of stones on the table.
# You and your friend will alternate taking turns, and you go first.
# On each turn, the person whose turn it is will remove 1 to 3 stones from the heap.
# The one who removes the last stone is the winner.
# Given n, the number of stones in the heap, return true if you can win the game assuming both you and your friend play optimally, otherwise return false.

 

# Example 1:

# Input: n = 4
# Output: false
# Explanation: These are the possible outcomes:
# 1. You remove 1 stone. Your friend removes 3 stones, including the last stone. Your friend wins.
# 2. You remove 2 stones. Your friend removes 2 stones, including the last stone. Your friend wins.
# 3. You remove 3 stones. Your friend removes the last stone. Your friend wins.
# In all outcomes, your friend wins.
# Example 2:

# Input: n = 1
# Output: true
# Example 3:

# Input: n = 2
# Output: true
 

# Constraints:

# 1 <= n <= 231 - 1

class Solution:
    def canWinNim(self, n: int) -> bool:
        return n % 4 != 0
    
# The core idea behind the Nim game with these rules (1 to 3 stones removed) is that if the number of stones n is a multiple of 4, 
# the second player (your friend) can always win.  This is because whatever number of stones you take (1, 2, or 3), your friend can 
# always take a number of stones that adds up to 4 in total for that round.

# Let's break it down:

# n % 4 == 0: If n is divisible by 4, no matter how many stones you take (1, 2, or 3), your friend can always choose a number of 
# stones to leave a multiple of 4 remaining.  Eventually, the number of stones will be 4, and no matter what you do, your friend 
# will take the remaining stones and win.

# n % 4 != 0: If n is not divisible by 4, you have a winning strategy.  You can always take a number of stones such that the remaining 
# number of stones is a multiple of 4.  Then, whatever your friend does, you can again make sure the remaining stones are a multiple of 4. 
# You continue this pattern.  Eventually, your friend will be left with 4 stones.  Whatever they do, you take the remaining stones and win.
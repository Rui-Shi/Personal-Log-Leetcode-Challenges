# An n-bit gray code sequence is a sequence of 2n integers where:

# Every integer is in the inclusive range [0, 2n - 1],
# The first integer is 0,
# An integer appears no more than once in the sequence,
# The binary representation of every pair of adjacent integers differs by exactly one bit, and
# The binary representation of the first and last integers differs by exactly one bit.
# Given an integer n, return any valid n-bit gray code sequence.

 

# Example 1:

# Input: n = 2
# Output: [0,1,3,2]
# Explanation:
# The binary representation of [0,1,3,2] is [00,01,11,10].
# - 00 and 01 differ by one bit
# - 01 and 11 differ by one bit
# - 11 and 10 differ by one bit
# - 10 and 00 differ by one bit
# [0,2,3,1] is also a valid gray code sequence, whose binary representation is [00,10,11,01].
# - 00 and 10 differ by one bit
# - 10 and 11 differ by one bit
# - 11 and 01 differ by one bit
# - 01 and 00 differ by one bit
# Example 2:

# Input: n = 1
# Output: [0,1]
 

# Constraints:

# 1 <= n <= 16

from typing import List

class Solution:
  def grayCode(self, n: int) -> List[int]:
    """
    Generates an n-bit Gray code sequence using the formula: i ^ (i >> 1).

    Args:
      n: The number of bits for the Gray code.

    Returns:
      A list of integers representing the n-bit Gray code sequence.
    """
    # The number of elements in an n-bit Gray code is 2^n.
    # 1 << n is an efficient way to calculate 2^n.
    # We iterate from i = 0 to (2^n - 1) and apply the formula.
    # A list comprehension provides a concise way to build the result.
    return [i ^ (i >> 1) for i in range(1 << n)]
        
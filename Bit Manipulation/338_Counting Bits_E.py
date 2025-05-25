# Given an integer n, return an array ans of length n + 1 such that for each i (0 <= i <= n), ans[i] is the number of 1's in the binary representation of i.

 

# Example 1:

# Input: n = 2
# Output: [0,1,1]
# Explanation:
# 0 --> 0
# 1 --> 1
# 2 --> 10
# Example 2:

# Input: n = 5
# Output: [0,1,1,2,1,2]
# Explanation:
# 0 --> 0
# 1 --> 1
# 2 --> 10
# 3 --> 11
# 4 --> 100
# 5 --> 101
 

# Constraints:

# 0 <= n <= 105

class Solution:
    def countBits(self, n: int) -> List[int]:
        result = []
        for i in range(n+1):
            binary_string = format(i, 'b') # convert a number to binary representation (string)
            binary_list = [int(char) for char in binary_string]
            result.append(sum(binary_list))
        return result

# another solution:
class Solution:
    def countBits(self, n: int) -> list[int]:
        """
        Calculates the number of set bits (1s) in the binary representation of each number
        from 0 to n (inclusive).

        Args:
            n: The upper limit of the range (inclusive).

        Returns:
            A list of integers where each element at index i represents the number of set bits
            in the binary representation of i.

        Example:
            countBits(5) returns [0, 1, 1, 2, 1, 2]
            because:
            0: 000 (0 set bits)
            1: 001 (1 set bit)
            2: 010 (1 set bit)
            3: 011 (2 set bits)
            4: 100 (1 set bit)
            5: 101 (2 set bits)

        Algorithm:
            Uses dynamic programming and bit manipulation.  The key idea is that the
            number of set bits in a number 'i' can be efficiently calculated using
            the number of set bits in 'i // 2' (integer division, equivalent to
            right-shifting the bits of 'i' by one: i >> 1) and the least significant
            bit (LSB) of 'i'.

            Specifically:
            ans[i] = ans[i >> 1] + (i & 1)

            - ans[i >> 1]:  The number of set bits in i // 2.  This value is already
                            computed in a previous iteration due to the dynamic
                            programming approach.
            - (i & 1):      This isolates the least significant bit (LSB) of 'i'.
                            It's 1 if 'i' is odd (LSB is 1), and 0 if 'i' is even
                            (LSB is 0).
            
            We add these two parts to efficiently derive the count of set bits for i.

        Time Complexity: O(n) - The loop iterates n times.
        Space Complexity: O(n) - The 'ans' list stores n+1 integers.
        """
        # Initialize a list to store the results. ans[i] will store the number of set bits in 'i'.
        ans = [0] * (n + 1)

        # Iterate from 1 to n (inclusive). ans[0] is already initialized to 0.
        for i in range(1, n + 1):
            # Calculate the number of set bits for the current number 'i' using dynamic programming:
            # 1. ans[i >> 1]: Get the count of set bits for i // 2 (right shift by 1).
            # 2. (i & 1):     Get the least significant bit of 'i' (1 if odd, 0 if even).
            # 3. Add the two values to get the total set bits for 'i'.
            ans[i] = ans[i >> 1] + (i & 1)

        return ans  # Return the list of set bit counts.
            
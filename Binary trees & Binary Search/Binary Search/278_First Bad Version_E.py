# You are a product manager and currently leading a team to develop a new product. Unfortunately, the latest version of your product fails the quality check. Since each version is developed based on the previous version, all the versions after a bad version are also bad.

# Suppose you have n versions [1, 2, ..., n] and you want to find out the first bad one, which causes all the following ones to be bad.

# You are given an API bool isBadVersion(version) which returns whether version is bad. Implement a function to find the first bad version. You should minimize the number of calls to the API.

 

# Example 1:

# Input: n = 5, bad = 4
# Output: 4
# Explanation:
# call isBadVersion(3) -> false
# call isBadVersion(5) -> true
# call isBadVersion(4) -> true
# Then 4 is the first bad version.
# Example 2:

# Input: n = 1, bad = 1
# Output: 1

# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        """
        Finds the first bad version in a range of versions [1, n].

        Args:
            n: The number of versions.

        Returns:
            The first bad version.
        """

        # Edge case: If the first version is bad, return 1
        if isBadVersion(1): 
            return 1 

        left = 1
        right = n

        # Binary search
        while right > left:  
            # Calculate the middle version
            mid = (left + right) // 2  

            # If the middle version is bad, search in the left half
            if isBadVersion(mid):  
                right = mid
            # Otherwise, search in the right half
            else:                 
                left = mid + 1
                
        # 'right' will hold the first bad version
        return left
                
        
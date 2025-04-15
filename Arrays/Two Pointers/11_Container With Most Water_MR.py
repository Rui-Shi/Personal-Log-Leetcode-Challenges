# You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).

# Find two lines that together with the x-axis form a container, such that the container contains the most water.

# Return the maximum amount of water a container can store.

# Notice that you may not slant the container.

 

# Example 1:


# Input: height = [1,8,6,2,5,4,8,3,7]
# Output: 49
# Explanation: The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7]. In this case, the max area of water (blue section) the container can contain is 49.
# Example 2:

# Input: height = [1,1]
# Output: 1

class Solution:
    def maxArea(self, height: List[int]) -> int:
        i = 0
        j = 0
        
        area = 0
        
        for i in range(len(height)-1):
            for j in range(i+1, len(height)):
                area_temp = (j-i)*min([height[i], height[j]])
                
                area = area_temp if area_temp > area else area
                
        return area
    
# a better one in O(n)
from typing import List

class Solution:
    def maxArea(self, height: List[int]) -> int:
        """
        Calculates the maximum area of water that can be contained between two vertical lines.

        Args:
            height: A list of non-negative integers representing the heights of the lines.

        Returns:
            The maximum area.
        """
        left = 0  # Left pointer, starting at the beginning of the list
        right = len(height) - 1  # Right pointer, starting at the end of the list
        max_area = 0

        while left < right:
            # Calculate the current area.  The width is (right - left).
            # The height is the MINIMUM of the two heights.
            current_area = (right - left) * min(height[left], height[right])

            # Update max_area if the current area is larger.
            max_area = max(max_area, current_area)

            # Move the pointer that points to the SHORTER line.
            # This is the crucial optimization step.
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1

        return max_area
# Why move the shorter pointer?  The key insight is that if we move the taller pointer, 
# the width of the container will decrease, and the height cannot increase (because it's limited by the shorter line).  
# Therefore, moving the taller pointer can only result in a smaller or equal area.  By moving the shorter pointer, 
# we have a chance of finding a taller line that might increase the area.

# Example Usage (for testing)
if __name__ == '__main__':
    solution = Solution()
    height1 = [1, 8, 6, 2, 5, 4, 8, 3, 7]
    print(f"Max area for {height1}: {solution.maxArea(height1)}")  # Output: 49

    height2 = [1, 1]
    print(f"Max area for {height2}: {solution.maxArea(height2)}")  # Output: 1

    height3 = [4, 3, 2, 1, 4]
    print(f"Max area for {height3}: {solution.maxArea(height3)}")  # Output: 16

    height4 = [1, 2, 1]
    print(f"Max area for {height4}: {solution.maxArea(height4)}") # Output: 2
        
        
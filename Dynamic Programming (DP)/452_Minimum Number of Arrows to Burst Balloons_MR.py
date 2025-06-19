# There are some spherical balloons taped onto a flat wall that represents the XY-plane. The balloons are represented as a 2D integer array points where points[i] = [xstart, xend] denotes a balloon whose horizontal diameter stretches between xstart and xend. You do not know the exact y-coordinates of the balloons.

# Arrows can be shot up directly vertically (in the positive y-direction) from different points along the x-axis. A balloon with xstart and xend is burst by an arrow shot at x if xstart <= x <= xend. There is no limit to the number of arrows that can be shot. A shot arrow keeps traveling up infinitely, bursting any balloons in its path.

# Given the array points, return the minimum number of arrows that must be shot to burst all balloons.

 

# Example 1:

# Input: points = [[10,16],[2,8],[1,6],[7,12]]
# Output: 2
# Explanation: The balloons can be burst by 2 arrows:
# - Shoot an arrow at x = 6, bursting the balloons [2,8] and [1,6].
# - Shoot an arrow at x = 11, bursting the balloons [10,16] and [7,12].
# Example 2:

# Input: points = [[1,2],[3,4],[5,6],[7,8]]
# Output: 4
# Explanation: One arrow needs to be shot for each balloon for a total of 4 arrows.
# Example 3:

# Input: points = [[1,2],[2,3],[3,4],[4,5]]
# Output: 2
# Explanation: The balloons can be burst by 2 arrows:
# - Shoot an arrow at x = 2, bursting the balloons [1,2] and [2,3].
# - Shoot an arrow at x = 4, bursting the balloons [3,4] and [4,5].
 

# Constraints:

# 1 <= points.length <= 105
# points[i].length == 2
# -231 <= xstart < xend <= 231 - 1

class Solution(object):
    def findMinArrowShots(self, points):
        # If there are no balloons, no arrows are needed.
        if not points:
            return 0

        # --- The Greedy Choice ---
        # Sort by the end points. This ensures we always handle the balloon
        # that finishes earliest, which is key to the greedy strategy.
        points.sort(key=lambda x: x[1])

        # We always need at least one arrow to start.
        arrows = 1
        # Place the first arrow at the end of the very first balloon.
        # This is the optimal position to maximize overlap with future balloons.
        end = points[0][1]

        # Iterate through the balloons to see how many new arrows are needed.
        for start, finish in points:
            # If the current balloon starts AFTER the last arrow's position...
            if start > end:
                # ...it cannot be burst by the previous arrow, so we need a new one.
                arrows += 1
                # Update the new arrow's position to the end of the current balloon.
                end = finish
        
        return arrows

# --- Example Walkthrough ---
# points = [[1, 6], [2, 8], [7, 12], [10, 16]]
# 1. Sort by end points: [[1, 6], [2, 8], [7, 12], [10, 16]] (already sorted in this case)
#
# 2. Initialize:
#    arrows = 1
#    end = 6  (end of the first balloon [1, 6])
#
# 3. Loop:
#    - Balloon [2, 8]: start is 2. Is 2 > 6? No. The arrow at x=6 can burst this balloon.
#    - Balloon [7, 12]: start is 7. Is 7 > 6? Yes. We need a new arrow.
#        - arrows becomes 2.
#        - Update end: end = 12.
#    - Balloon [10, 16]: start is 10. Is 10 > 12? No. The arrow at x=12 can burst this one.
#
# 4. End of loop. Return arrows, which is 2.
        
        
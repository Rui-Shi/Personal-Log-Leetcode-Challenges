# find the largest sum of a subarray of an array

def largestsum(nums):
    max_so_far = 0  # Initialize the overall maximum sum
    current_max = 0  # Initialize the maximum sum for the current subarray
    for num in nums:
        if num > 0:
            current_max += num  # Add to current sum if positive
        else:
            current_max = 0  # Reset current sum if negative or zero

        max_so_far = max(max_so_far, current_max)  # Update overall max

    return max_so_far

a =  [-1,-3,5,-4,3,-6,9,2]
b =  [-1,-3,5,-4,3,-6,-9,2]
print(largestsum(a))
print(largestsum(b))
            
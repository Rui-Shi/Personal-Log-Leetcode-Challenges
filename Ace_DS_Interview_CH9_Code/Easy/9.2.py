# Return the maximum product of any three numbers in a array

# Solution: use heap
import heapq

def max_three(arr):
    a = heapq.nlargest(3, arr) # largest 3 numbers
    b = heapq.nsmallest(2, arr) # smallest 2 (for negatives case)
    return max(a[0]*a[1]*a[2], b[1]*b[0]*a[0])

print(max_three([-2, -4, 5, 3]))
    
    
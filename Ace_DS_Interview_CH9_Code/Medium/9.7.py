# Find the peaks in a list of numbers

# My solution
def find_peak(nums: list) -> list:
    res = []
    i = 1
    while i < len(nums)-1:
        if nums[i] > max(nums[i-1], nums[i+1]):
            res.append(i)
            i += 2
        else:
            i += 1
    return res

a = [3, 5, 2, 4, 1]
print(find_peak([3, 5, 2, 4, 1]))


# Solutions (using binary search)
def get_peak(arr):
    left = 0
    right = len(arr) - 1
    
    while True:
        mid = (left + right) // 2
        left = arr[mid-1]
        right = arr[mid+1]
        
        if left < arr[mid] and right < arr[mid]:
            return arr[mid]
        elif left > arr[mid]:
            right = mid - 1
        else:
            left = mid + 1
        
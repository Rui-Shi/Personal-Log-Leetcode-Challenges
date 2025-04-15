# Intersections between 2 arrays

# My Solution:
def intersection(a, b):
    res = []
    for num in a:
        if num in b:
            res.append(num)
    return res

print(intersection([1,2,3], [3,4,5]))

# Solution (better, using sets to reduce the time complexity)
def intersection(a, b):
    set_a = set(a)
    set_b = set(b)
    if len(set_a) < len(set_b):
        return [x for x in set_a if x in set_b]
    else:
        return [x for x in set_b if x in set_a]
    
print(intersection([1,2,3], [3,4,5]))
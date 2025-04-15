# find the k smallest value in a sorted matrix
from heapq import heappush, heappop

def smallest(m, k):
    n = len(m)
    heap = [] # heap
    res = -1
    for i in range(min(n,k)):
        for j in range(min(n,k)):
            heappush(heap, m[i][j])
    for i in range(k):
        res = heappop(heap)
    return res


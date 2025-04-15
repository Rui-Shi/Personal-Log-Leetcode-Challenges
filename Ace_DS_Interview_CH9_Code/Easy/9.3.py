# find the k closest points to the origin

from heapq import heappush, heappop

def closest_points(pts, k):
    min_heap = []
    res = []
    for pt in pts:
        heappush(min_heatp, (sum([x**2 for x in pt]), pts)) # adds a tuple to the min_heap, sort from small to large based on the first element
    for i in range(k):
        res.append(heapop(min_heap[1])) # get top k
    return res
        

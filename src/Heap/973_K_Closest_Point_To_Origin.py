import math, heapq

def kClosest(points, K):
    heap = []

    res = []
    for point in points:                                        
        distance = calculateDistance(point[0], point[1])
        heapq.heappush(heap, (distance, point))
    while K:                                                    
        res.append(heapq.heappop(heap)[1])
        K -= 1
    return res

def calculateDistance(x, y):
    return math.sqrt(x**2+y**2)
        
points = [[1,3],[-2,2]]
K = 1

print(kClosest(points, K))

#https://leetcode.com/problems/k-closest-points-to-origin/
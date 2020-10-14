# Solution 1: Using heap with runtime complexity of O(nlogk) and space O(n) -> there exists a better solution quick selection O(n)

import collections, heapq

def topKElementHeap(nums, k):
    count = collections.Counter(nums)
    heap = []
    res = []
        
    for key in count:
        heapq.heappush(heap, (-count[key], key))
    for _ in range(k):
        count, item = heapq.heappop(heap)
        res.append(item)
    return res

nums = [1,1,1,2,2,3]
k = 2
print(topKElementHeap(nums,k))

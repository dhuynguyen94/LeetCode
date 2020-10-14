# Solution 1: Using heap and dictionary -> Run time complexity: O(nlogn), space O(n)
import heapq, collections
def frequencySortHeap(s):
    if not s:
        return s
    counter = collections.Counter(s)
    res = ""
    heap = []
    for element in counter:
        heapq.heappush(heap, (-counter[element], element))
    
    while heap:
        count, char = heapq.heappop(heap)
        for _ in range(abs(count)):
            res += char

    return res

# Time complexity: O(nlogn)
# Space complexity O(n)


# Solution 2: Using bucket sort 
def frequencySortBucket(s):
    if not s:
        return s
    counter = collections.Counter(s)
    res = ""
    max_freq = max(counter.values())

    buckets = [[] for _ in range(max_freq+1)]

    for key in counter:
        count = counter[key]
        buckets[count].append(key)

    for i in range(len(buckets)-1, 0, -1):
        for char in buckets[i]:
            for _ in range(i):
                res += char
    return res


# Time complexity: O(n)
# Space complexity O(n)
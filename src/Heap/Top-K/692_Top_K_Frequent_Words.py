# https://leetcode.com/problems/top-k-frequent-words/

import collections, heapq
def topKFrequent(self, words: List[str], k: int) -> List[str]:
    #  Create a dictionary of word: count
    counter = collections.Counter(words)    #O(n) space complexity + #O(n) time complexity
        
    heap = []                   #O(n) space complexity

    # pushing in negative value of count because heapq in python is default to a min heap.
    for key in counter:         #O(n) runtime complexity
        heapq.heappush(heap, (-counter[key], key))  #O(logn) runtime complexity
    res =[]
    for _ in range(k):          #O(n) space complexity
        count, element = heapq.heappop(heap) #O(logn) runtime complexity
        res.append(element)
    return res

# Time Complexity: O(nlogn)
# Space Complexity: O(n)
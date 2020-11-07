class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        count = collections.Counter(nums)
        heap, ret = [], []
        for key, val in count.items():
            heapq.heappush(heap, (-val, key))
        for _ in range(k):
            ret.append(heapq.heappop(heap)[1])
        return ret


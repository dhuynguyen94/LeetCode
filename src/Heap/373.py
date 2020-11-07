class Solution(object):
    def kSmallestPairs(self, nums1, nums2, k):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :type k: int
        :rtype: List[List[int]]
        """
        if not len(nums1) or not len(nums2):
            return []
        heap = []
        for val1 in nums1:
            for val2 in nums2:
                heapq.heappush(heap, (val1 + val2, [val1, val2]))
        ret = []
        for i in range(k):
            if len(heap) == 0:
                return ret
            ret.append(heapq.heappop(heap)[1])
        return ret


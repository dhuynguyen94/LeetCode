class Solution(object):
    def kthSmallest(self, matrix, k):
        """
        :type matrix: List[List[int]]
        :type k: int
        :rtype: int
        """
        heap = []
        for row in matrix:
            for num in row:
                heapq.heappush(heap, num)
        for _ in range(k - 1):
            heapq.heappop(heap)
        return heap[0]

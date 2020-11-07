class Solution(object):
    def lastStoneWeight(self, stones):
        """
        :type stones: List[int]
        :rtype: int
        """
        for i in range(len(stones)):
            stones[i] *= -1

        heapq.heapify(stones)

        while (len(stones) > 1):
            first_stone = heapq.heappop(stones)
            second_stone = heapq.heappop(stones)
            if first_stone != second_stone:
                val = -abs(first_stone - second_stone)
                heapq.heappush(stones, val)

        if len(stones) == 0:
            return 0
        return -stones[0]

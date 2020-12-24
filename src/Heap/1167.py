class Solution:
    def connectSticks(self, sticks: List[int]) -> int:
        heapq.heapify(sticks)
        ans = 0
        while len(sticks) != 1:
            val1 = heapq.heappop(sticks)
            val2 = heapq.heappop(sticks)
            sum_t = val1 + val2
            ans += sum_t
            heapq.heappush(sticks, sum_t)
        return ans

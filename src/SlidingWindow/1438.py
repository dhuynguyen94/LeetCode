class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        minHeap, maxHeap = [], []
        j, ans = 0, 0
        for i in range(len(nums)):
            heapq.heappush(minHeap, (nums[i], i))
            heapq.heappush(maxHeap, (-nums[i], i))

            while nums[i] - minHeap[0][0] > limit: # Shrink the Window
                minValue = heapq.heappop(minHeap)
                j = max(j, minValue[1] + 1)
            while -maxHeap[0][0]-nums[i] > limit: #  Shrink the Window
                maxValue = heapq.heappop(maxHeap)
                j = max(j, maxValue[1] + 1)
            ans = max(ans, i - j + 1)
        return ans

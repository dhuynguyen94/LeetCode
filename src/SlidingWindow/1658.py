class Solution:
    def minOperations(self, nums: List[int], x: int) -> int:
        max_sub = sum(nums) - x
        start, ans, sum_t, n = 0, -1, 0, len(nums)
        for end in range(len(nums)):
            sum_t += nums[end]
            while sum_t > max_sub and start <= end:
                sum_t -= nums[start]
                start += 1
            if sum_t == max_sub:
                ans = max(ans, end - start + 1)
        return n - ans if ans != -1 else -1

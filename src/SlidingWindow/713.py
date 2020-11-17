class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        if k <= 1: return 0
        j, ans = 0, 0
        product = 1
        for i in range(len(nums)):
            product *= nums[i]
            while product >= k:
                product = product / nums[j]
                j += 1
            ans += i - j + 1
        return ans

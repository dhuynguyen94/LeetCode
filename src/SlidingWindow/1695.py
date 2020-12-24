class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        max_t = 0
        ans = 0
        j = 0
        dict_t = collections.defaultdict(int)
        for i in range(len(nums)):
            ans += nums[i]
            dict_t[nums[i]] += 1
            while j < len(nums) and dict_t[nums[i]] > 1:
                ans -= nums[j]
                dict_t[nums[j]] -= 1
                j += 1
            max_t = max(ans, max_t)
        return max_t

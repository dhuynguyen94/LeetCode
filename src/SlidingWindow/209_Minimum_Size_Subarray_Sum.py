def minSubArrayLen(self, s: int, nums: List[int]) -> int:
    min_len = math.inf
    cur_sum = 0
    start = 0
    for end, n in enumerate(nums):
        cur_sum += n
        while cur_sum >= s:
            min_len = min(min_len, end-start+1)
            cur_sum -= nums[start]
            start += 1
    return min_len if min_len != math.inf else 0


# Note:
# Time Complexity: O(n)
# Space Complexity: O(1)
# Link to LC : https://leetcode.com/problems/minimum-size-subarray-sum/
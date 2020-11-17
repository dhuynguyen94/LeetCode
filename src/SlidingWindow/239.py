# Node: Time Limit Exceeded
class Solution(object):
    def maxSlidingWindow(self, nums, k):
        max_t = max(nums[0:k])
        n = len(nums)
        ret = [max_t]
        for i in range(n-k):
            j = i + k
            if nums[j] >= max_t:
                max_t = nums[j]
            elif nums[i] == max_t:
                max_t = max(nums[i+1:j+1])

            ret.append(max_t)
        return ret


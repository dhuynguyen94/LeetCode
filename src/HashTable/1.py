class Solution:
    # Using map
    def twoSum(self, num, target):
        map = {}
        for i in range(len(num)):
            if num[i] not in map:
                map[target - num[i]] = i + 1
            else:
                return map[num[i]], i + 1

        return -1, -1

    # Using Two pointer
    def twoSum(self, nums, target):
        nums = sorted(nums)
        start = 0
        end = len(nums) - 1
        while start < end:
            mysum = nums[start] + nums[end]
            if mysum == target:
                return [start, end]
            elif mysum > target:
                end -= 1
            else:
                start += 1

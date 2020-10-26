class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        start, end = 0, len(nums) - 1
        while start <= end:
            mid = start + (end - start) // 2
            if nums[mid] == target:
                return mid
            elif nums[start] < nums[mid]: # left side is sorted
                if nums[start] <= target <= nums[mid]:
                    end = mid - 1
                else:
                    start = mid + 1
            elif nums[start] > nums[mid]: # right side is sorted
                if nums[mid] <=target <= nums[end]:
                    start = mid + 1
                else:
                    end = mid -1
            else:
                start = mid + 1
        return -1

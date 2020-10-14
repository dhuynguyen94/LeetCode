class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        result = []
        self.BackTrackPermuteUnique(nums,result,0)
        A = []
        for item in result:
            if item not in A:
                A.append(item)
        return A
    def BackTrackPermuteUnique(self,nums,result,index):
        if index == len(nums):
            result.append(nums[:])
            return
        for i in range(index,len(nums)):
            nums[i],nums[index] = nums[index],nums[i]
            self.BackTrackPermuteUnique(nums,result,index+1)
            nums[i],nums[index] = nums[index],nums[i]
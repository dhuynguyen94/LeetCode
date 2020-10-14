# Time complexity : N * N!
# Space Complexity: N * N!

## First Way
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = []
        self.dfs(nums, result, [], [])
        return result

    def dfs(self, nums, result, ans, visited):
        if len(ans) == len(nums):
            result.append(ans[:])
            return

        for item in nums:  # 1,2,3
            if item in visited:
                continue
            visited.append(item)  # visited = {1}
            ans.append(item)
            self.dfs(nums, result, ans, visited)
            ans.pop()
            visited.pop()

## Second way
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = []
        self.BackTrackPermute(nums,result,0)
        return result
    def BackTrackPermute(self,nums,result,index):
        if index == len(nums):
            result.append(nums[:])
            return
        for i in range(index,len(nums)):
            nums[i],nums[index] = nums[index],nums[i]
            self.BackTrackPermute(nums,result,index+1)
            nums[i],nums[index] = nums[index],nums[i]

class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        result = set()
        nums1 = sorted(nums)
        self.backtrackSubsetsWithDup(result,nums1,[],0)
        return result
    def backtrackSubsetsWithDup(self,result,nums,path,index):
        result.add(tuple(path))
        # backtrack function
        for i in range(index,len(nums)):
            path.append(nums[i])
            self.backtrackSubsetsWithDup(result,nums,path,i+1)
            path.pop()



# Another way
class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        self.ans = [[]]
        nums.sort()
        for i in range(1, len(nums)+1):
            self.backtracking(nums, i, [], 0)

        return self.ans

    def backtracking(self, nums, size, path, idx):
        if len(path) == size:
            self.ans.append(path[:])
            return

        for i in range(idx, len(nums)):
            if i > idx and nums[i] == nums[i-1]:
                continue
            path.append(nums[i])
            self.backtracking(nums, size, path, i+1)
            path.pop()


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
    
        

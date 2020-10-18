class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = []
        self.backtrackSubsets(nums,result,[],0)
        return result
    def backtrackSubsets(self,nums,result,path,index):
        # if condition
        result.append(path[:])
        #backtrack function 
        for i in range(index,len(nums)):
            path.append(nums[i])
            self.backtrackSubsets(nums,result,path,i+1)
            path.pop()

class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        mycandidates = sorted(candidates)
        result = []
        self.BackTrackingCombinationSum2(mycandidates, target, result, [], 0)
        return result

    def BackTrackingCombinationSum2(self, mycandidates, target, result, path, index):
        ## if condition
        if target == 0:
            result.append(tuple(path))
            return
        elif target < 0:
            return
        # Backtrack
        for i in range(index, len(mycandidates)):
            path.append(mycandidates[i])
            self.BackTrackingCombinationSum2(mycandidates, target - mycandidates[i], result, path, i + 1)
            path.pop()


# Another way
class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        self.ans = []
        self.backtracking(candidates, target, [], 0)
        return self.ans

    def backtracking(self, candidates, target, path, idx):
        if target < 0:
            return
        if target == 0:
            self.ans.append(path[:])
        for i in range(idx, len(candidates)):
            if i > idx and candidates[i] == candidates[i-1]:
                continue
            path.append(candidates[i])
            self.backtracking(candidates, target-candidates[i], path, i+1)
            path.pop()


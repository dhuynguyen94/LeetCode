class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        mycandidates = sorted(candidates)
        result = []
        self.BackTrackingCombinationSum2(mycandidates, target, result, [], 0)
        return result

    def BackTrackingCombinationSum2(self, mycandidates, target, result, path, index):
        ## if condition
        if target == 0:
            result.a(tuple(path))
            return
        elif target < 0:
            return
        # Backtrack
        for i in range(index, len(mycandidates)):
            path.append(mycandidates[i])
            self.BackTrackingCombinationSum2(mycandidates, target - mycandidates[i], result, path, i + 1)
            path.pop()


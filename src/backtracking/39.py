# Time complexity : N * N!/(N−k)!k!
# Space Complexity: N * N!/(N−k)!k!
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []
        if len(candidates) == 0:
            return []
        self.BackTrackCombinationSum(candidates, target, [], result)
        print(result)
        return result

    def BackTrackCombinationSum(self, candidates, target, path, result):
        # condition
        if target == 0:
            result.append(path[:])
            return
        if target < 0:
            return
        for i in range(len(candidates)):
            path.append(candidates[i])
            self.BackTrackCombinationSum(candidates[i:], target - candidates[i], path, result)
            path.pop()











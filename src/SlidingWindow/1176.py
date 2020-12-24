class Solution:
    def dietPlanPerformance(self, calories: List[int], k: int, lower: int, upper: int) -> int:
        sum_t = sum(calories[:k])
        j, ans = 0, 0
        if sum_t < lower: ans = -1
        if sum_t > upper: ans = 1
        for i in range(k, len(calories)):
            sum_t -= calories[j]
            sum_t += calories[i]
            j += 1
            if sum_t < lower: ans -= 1
            if sum_t > upper: ans += 1

        return ans


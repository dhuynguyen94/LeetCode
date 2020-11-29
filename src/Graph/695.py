class Solution:
    def dfs(self, grid, row, col):
        if row < 0 or row >= len(grid) or col < 0 or col >= len(grid[row]):
            return 0
        if grid[row][col] == 0 or grid[row][col] == 'X':
            return 0
        grid[row][col] = 'X'
        return 1 + self.dfs(grid, row - 1, col) + self.dfs(grid, row + 1, col) + self.dfs(grid, row, col - 1) + self.dfs(grid, row, col + 1)

    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        ans = []
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                count = self.dfs(grid, i, j)
                ans.append(count)
        return max(ans)

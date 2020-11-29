class Solution:
    def dfs(self, grid, row, col):
        if row < 0 or row >= len(grid) or col < 0 or col >= len(grid[row]):
            return
        if grid[row][col] == 1:
            return
        grid[row][col] = 1
        self.dfs(grid, row - 1, col)
        self.dfs(grid, row + 1, col)
        self.dfs(grid, row, col - 1)
        self.dfs(grid, row, col + 1)

    def closedIsland(self, grid: List[List[int]]) -> int:
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if i == 0 or j == 0 or j == len(grid[-1])-1 or i == len(grid)-1:
                    self.dfs(grid, i, j)  # Mark all boundary by 1
        count = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 0:
                    self.dfs(grid, i, j)
                    count += 1

        return count

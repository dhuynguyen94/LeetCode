class Solution:
    def helper(self, grid, row, col):
        if row < 0 or row >= len(grid) or col < 0 or col >= len(grid[row]):
            return
        if grid[row][col] == 'x' or grid[row][col] == '0':
            return
        grid[row][col] = 'x'
        self.helper(grid, row +1, col)
        self.helper(grid, row - 1, col)
        self.helper(grid, row, col + 1)
        self.helper(grid, row, col - 1)


    def numIslands(self, grid: List[List[str]]) -> int:
        ans = 0
        for row in range(len(grid)):
            for col in range(len(grid[row])):
                if (grid[row][col] == '1'):
                    self.helper(grid, row, col)
                    ans += 1
        return ans

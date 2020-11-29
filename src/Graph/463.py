class Solution(object):
    def move(self, grid, row, col):
        if row < 0 or row >= len(grid) or col < 0 or col >= len(grid[row]):
            return 1
        if grid[row][col] == 0:
            return 1
        if grid[row][col] == 'X':
            return 0
        grid[row][col] = 'X'
        return self.move(grid, row -1, col) + self.move(grid, row + 1, col) + self.move(grid, row, col - 1) + self.move(grid, row, col + 1)
    def islandPerimeter(self, grid):
        ans = 0
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == 1:
                    ans += self.move(grid, i, j)
        return ans


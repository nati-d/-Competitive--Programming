class Solution:
    def maxIncreaseKeepingSkyline(self, grid: List[List[int]]) -> int:
        n = len(grid)
        sm = 0
        maxCols = [0] * n

        for i in range(n):
            for j in range(n):
                maxCols[j] = max(maxCols[j], grid[i][j])
        

        for i in range(n):
            localMax = max(grid[i])
            for j in range(n):
                sm += abs(min(localMax,maxCols[j]) - grid[i][j])
        

        print()
        return sm
        
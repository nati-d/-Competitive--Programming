class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.grid = [[0]*len(matrix[0]) for i in range(len(matrix))]
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if i == 0:
                    if j == 0:
                        self.grid[i][j] = matrix[i][j]
                    else:
                        self.grid[i][j] = self.grid[i][j-1] + matrix[i][j]
                else:
                    if j == 0:
                        self.grid[i][j] = self.grid[i-1][j] + matrix[i][j]
                    else:
                        self.grid[i][j] = self.grid[i-1][j] + self.grid[i][j-1] + matrix[i][j] - self.grid[i-1][j-1]

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        top = self.grid[row1-1][col2] if row1 > 0 else 0
        left = self.grid[row2][col1-1] if col1 > 0 else 0
        overlap = self.grid[row1-1][col1-1] if row1 > 0 and col1 > 0 else 0

        return self.grid[row2][col2] - top - left + overlap

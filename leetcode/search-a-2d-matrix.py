class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows = []

        for row in range(len(matrix)):
            rows.append(matrix[row][0])
        print(rows)

        left = -1
        right = len(rows)
        ind = 0

        while left+1 < right:
            mid = (left+right)//2
            if rows[mid] > target:
                right = mid
            else:
                ind = max(ind,mid)
                left = mid
        print(ind)
        left = -1
        right = len(matrix[0])

        while left+1 < right:
            mid = (left+right)//2
            if matrix[ind][mid] == target:
                return True
            elif matrix[ind][mid] > target:
                right = mid
            else:
                left = mid
        return False

        
class Solution:
    def numSubmatrixSumTarget(self, matrix: List[List[int]], target: int) -> int:
        m, n = len(matrix), len(matrix[0])
        count = 0

        for row in matrix:
            for j in range(1, n):
                row[j] += row[j - 1]

        for left in range(n):
            for right in range(left, n):
                psum = {0: 1}
                cur = 0
                for row in matrix:
                    cur += row[right] - (row[left - 1] if left > 0 else 0)
                    count += psum.get(cur - target, 0)
                    psum[cur] = psum.get(cur, 0) + 1

        return count
class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:

        t = []

        for c in range(len(matrix[0])):
            k = []
            for r in range(len(matrix)):
                k.append(matrix[r][c])
            t.append(k)
        return t
                

        
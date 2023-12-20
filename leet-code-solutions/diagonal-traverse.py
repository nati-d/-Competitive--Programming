class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        dic = defaultdict(list)
        res = []

        for r in range(len(mat)):
            for c in range(len(mat[0])):
                key = r+c
                dic[key].append(mat[r][c])
        for key,values in dic.items():
            if key%2 == 0:
                dic[key].reverse()
        for key, values in dic.items():
            res.extend(values)
        return res
        
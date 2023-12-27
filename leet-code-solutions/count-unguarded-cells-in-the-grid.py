class Solution:
    def countUnguarded(self, m: int, n: int, guards: List[List[int]], walls: List[List[int]]) -> int:

        mat = [['a']* n for _ in range(m)]
        res = []

        for g in guards:
            mat[g[0]][g[1]] = 'G'
        for w in walls:
            mat[w[0]][w[1]] = 'W'
        
        for g in guards:
            r = g[0] -1
            c = g[1]

            while r >=0 :
                if (mat[r][c] == 'W' or mat[r][c] == 'G'):
                    break
                else:
                    mat[r][c] = 'c'
                    r-=1
            r = g[0]+1
            c = g[1]
            while r <len(mat) :
                if (mat[r][c] == 'W' or mat[r][c] == 'G'):
                    break
                else:
                    mat[r][c] = 'c'
                    r+=1
            r = g[0] 
            c = g[1] -1

            while c >=0 :
                if (mat[r][c] == 'W' or mat[r][c] == 'G'):
                    break
                else:
                    mat[r][c] = 'c'
                    c-=1
            r = g[0]
            c = g[1] + 1
            while c <len(mat[0]) :
                if (mat[r][c] == 'W' or mat[r][c] == 'G'):
                    break
                else:
                    mat[r][c] = 'c'
                    c+=1
        print(mat)
        for i in mat:
            res.extend(i)
        return res.count('a')
        
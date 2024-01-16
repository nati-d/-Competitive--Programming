class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        N = len(s)
        k = len(shifts)
        alp = "abcdefghijklmnopqrstuvwxyz"

        p = [0]* N
        for st,e,d in shifts:
            if d == 0:
                p[st] -= 1
                if e+1 < N:
                    p[e+1] += 1
            else:
                p[st] += 1
                if e+1 < N:
                    p[e+1] -= 1
        sm =[p[0]]


        for i in range(1,len(p)):
            sm.append(sm[i-1] + p[i])

        
        for i in range(len(sm)):
            sm[i] += alp.index(s[i])
            ans = []
        for i in range(len(sm)):
            key = sm[i] % 26
            ans.append(alp[key])
        return "".join(ans)

        
        

class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        
        N = len(s)
        k = len(p)
        r = k
        l = 0
        ans = []
        temp = []
        c = 0
        dct = Counter(s[:k])
        cnt_p = Counter(p)

        while r<=N:
            if dct == cnt_p:
                ans.append(l)
            dct[s[l]] -= 1
            if dct[s[l]] == 0:
                del dct[s[l]]
            if r< N:
                dct[s[r]] += 1
            l+=1
            r+=1
        return ans
                





        N = len(s)
        k = len(p)
        ans = []
        l =0
        r = k-1

        tp = list(p)
        tp.sort()

        while l<= N-k:
            tm = s[l:r+1]
            tm = list(tm)
            tm.sort()
            if tm == tp:
                ans.append(l)
            l+=1
            r+=1
        return ans

        
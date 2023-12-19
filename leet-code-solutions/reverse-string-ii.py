class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        words = list(s)
        i = 0
        res = []
        while i < len(words):
            if i % (2*k) == 0 : 
                temp = words[i:i+k][::-1]
                for j in temp:
                    res.append(j)
                i+=k
            else:
                res.append(words[i])
                i+=1
        return "".join(res)

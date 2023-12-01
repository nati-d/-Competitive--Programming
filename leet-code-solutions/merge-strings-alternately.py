class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        mn = min(len(word1), len(word2))
        res=[]
        for i in range(mn):
            res.append(word1[i])
            res.append(word2[i])
        res.append(word1[mn::])
        res.append(word2[mn::])

        return "".join(res)
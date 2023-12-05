class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        word = list(s)
        st =""
        for i in range(len(indices)):
            n = indices.index(i)
            st+=word[n]
        return st
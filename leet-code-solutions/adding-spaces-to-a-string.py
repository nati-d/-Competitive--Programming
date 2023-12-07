class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        
        res = []
        c = 0
        for space in spaces:
            res.append(s[c:space])
            c = space
        res.append(s[c:])
       
        return " ".join(res)
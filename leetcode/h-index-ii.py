class Solution:
    def hIndex(self, citations: List[int]) -> int:

        for i in range(len(citations),0,-1):
            if i <= citations[len(citations)-i]:
                return i
        return 0
                      
       
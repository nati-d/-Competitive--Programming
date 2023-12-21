class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        count = 0
        for i in zip(*strs):
            k = sorted(i)
            if k != list(i):
                count+=1
            
        return count
        

        
class Solution:
    def escapeGhosts(self, ghosts: List[List[int]], target: List[int]) -> bool:
        pd = abs(target[0])+abs(target[1])
        for i in range(len(ghosts)):
           gd = abs(ghosts[i][0]-target[0])+abs(ghosts[i][1]-target[1])
           if gd <= pd:
               return False
           
        return True
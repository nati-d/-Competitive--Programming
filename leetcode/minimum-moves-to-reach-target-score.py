class Solution:
    def minMoves(self, target: int, maxDoubles: int) -> int:
        ans = 0
        sm = target
        while maxDoubles > 0 and sm > 1:
            if sm % 2 ==1:
                ans += 1
                sm-=1
            else:
                maxDoubles -= 1
                sm-= sm//2
                ans += 1
            
        
        ans += sm-1
        return ans
        
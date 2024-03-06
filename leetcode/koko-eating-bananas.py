class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left = 0
        right = sum(piles)+1

        def checker(k):
            count = 0
            for i in range(len(piles)):
                count+= ceil(piles[i]/k)
            return count
        
        while left+1 < right:
            mid = (left+right) // 2
            if checker(mid) <= h:
                right = mid
            else:
                left = mid
        return left+1
                

        
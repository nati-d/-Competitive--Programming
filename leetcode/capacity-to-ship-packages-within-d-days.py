class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        left = max(weights) -1
        right = sum(weights)+1
        mnn = right


        def checker(curr,days):
            count = 1
            sm = 0
            arr = []

            for i in range(len(weights)):
                if sm + weights[i] <= curr:
                    sm+=weights[i]
                else:
                    count +=1
                    sm = 0
                    sm+=weights[i]
            return count
        while left +1 < right:
            mid = (left+right)//2
            if checker(mid,days) <= days:
                mnn = min(mnn,mid)
                right = mid
            else:
                left = mid

        return mnn




        
        
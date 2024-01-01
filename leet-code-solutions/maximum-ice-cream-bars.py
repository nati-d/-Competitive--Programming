class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        costs.sort()
        sum =0
        count = 0
        for i in range(len(costs)):
            sum+=costs[i]
            if sum <= coins:
                count+=1
            if sum >= coins:
                break
        return count

       


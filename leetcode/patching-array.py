class Solution:
    def minPatches(self, nums: List[int], n: int) -> int:
        sm = 0
        cost = 0
        for num in nums:
            if num > n:
                break
            while num - 1 > sm:
                sm += sm + 1
                cost += 1
            sm += num
        while n > sm:
            sm += sm + 1
            cost += 1
        return cost


              

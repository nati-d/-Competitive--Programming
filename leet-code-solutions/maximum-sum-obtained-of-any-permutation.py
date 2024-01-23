class Solution:
    def maxSumRangeQuery(self, nums: List[int], requests: List[List[int]]) -> int:
        N = len(nums)
        p =[0] * N

        for first,last in requests:
            p[first] += 1
            if last+1 < N:
                p[last+1] -= 1
        for i in range(1,N):
            p[i] = p[i] + p[i-1]
        p.sort(reverse = True)
        nums.sort(reverse = True)
        
        sm = 0
        for i in range(N):
            sm += (p[i] * nums[i]) 
        return sm % ((10**9) + 7)


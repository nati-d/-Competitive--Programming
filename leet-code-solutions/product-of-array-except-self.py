class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        N = len(nums)
        suffix = [1] * N
        prefix = [1] * N
        ans = [0] * N

        pro = 1

        for i in range(N):
            pro *= nums[i]
            prefix[i] = pro 

        pro = 1
        for i in range(N-1,-1,-1):
            pro *= nums[i]
            suffix[i] = pro 
        for i in range(N):
            if i == 0:
                ans[i] = suffix[i+1]
            elif i == N-1:
                ans[i] = prefix[i-1]
            else:
                ans[i] = prefix[i-1] * suffix[i+1]
        return ans

        
class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        # l=0
        # r=0
        # mx=0

        # while r <len(nums):
        #     if nums[r]==1:
        #         r+=1
        #     else:
        #         mx=max(mx,r-l)
        #         l=r+1
        #         r+=1
        # mx = max(mx,r-l)
        # return mx


        return len(max(list(map(str,''.join(map(str,nums)).split('0')))))
        
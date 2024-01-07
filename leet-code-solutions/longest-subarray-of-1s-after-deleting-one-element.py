class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        l,r=0,0
        N = len(nums)
        cz = 0
        mx = 0

        while r<N:
            if nums[r] == 0:
                cz +=1
            r+=1

            # print(r,l)
            # print(cz)
            while cz >1:
                if nums[l] == 0:
                    cz-=1
                l+=1
            mx = max(mx, r-l-1)

            
        return mx


        
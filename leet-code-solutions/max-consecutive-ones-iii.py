class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        cz = 0
        l =0
        r = 0
        mx =0
        N = len(nums)

        while r<N:
            if nums[r] == 0 :
                cz +=1
            r+=1

            while cz > k and l<r:
                if nums[l] == 0:
                    cz-=1
                l+=1
            mx = max(mx, r-l)
        return mx
        
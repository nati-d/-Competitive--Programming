class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        mx = -inf
        l,r = 0,1
        N = len(nums)
        sm = sum(nums[:k])
        mx = max(mx,sm/k)
        print(sm,mx)

        while r<=N-k:
            print(l,r)
            sm += nums[l+k]
            sm -= nums[r-1]
            print(sm)
            mx = max(mx, sm/k)
            r+=1
            l+=1
        return mx



        
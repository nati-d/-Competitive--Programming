class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        N = len(nums)
        l =0 
        r = N-1
        sm = 0
        df = 20000

        for i in range(N):
            if i>0 and nums[i] == nums[i-1]:
                continue
            
            l,r = i+1, N-1

            while l<r:
                s = nums[i] + nums[l] + nums[r]
                if abs(s - target) < df:
                    df = abs(s - target)
                    sm = s
                if s > target:
                    r-=1
                elif s < target:
                    l+=1
                else:
                    sm = s
                    break
        return sm
                

    
        
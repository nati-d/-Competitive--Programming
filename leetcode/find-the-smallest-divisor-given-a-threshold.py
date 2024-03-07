class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        left = 0
        right = max(nums) +1
        nums.sort()

        def checker(thres):
            sm = 0
            for i in range(len(nums)):
                sm += ceil(nums[i]/thres)
            print(sm)
            
            return sm
        
        while left+1 < right:
            mid = (left+right)//2
            val = checker(mid)
            print(mid,val)

            if val > threshold:
                left = mid
            else:
                right = mid
        return right
        
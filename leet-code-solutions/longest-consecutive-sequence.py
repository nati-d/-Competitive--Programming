class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums.sort()
        count =1
        r=1
        maxx = 0

        if len(nums)<1:
            return 0

        while r<len(nums):
            if nums[r]-nums[r-1] ==0:
                r+=1
                continue
            elif nums[r]-nums[r-1] ==1:
                count+=1
            else:
                maxx = max(maxx,count)
                count =1
            r+=1
        maxx = max(maxx,count)

        return maxx
                

             
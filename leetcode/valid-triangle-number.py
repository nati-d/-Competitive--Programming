class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        n = len(nums)
        nums.sort()
        print(nums)
        count = 0



        for i in range(len(nums)):
            if nums[i] == 0:
                continue
            for j in range(i+1,len(nums)):
                if nums[j] == 0:
                    continue
                sm = nums[i] + nums[j]
                ind = bisect.bisect_left(nums,sm)
                count+= ind - (j+1)
                


        return count
        
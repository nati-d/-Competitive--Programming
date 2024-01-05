class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        ans = []
        nums.sort()

        for i in range(len(nums)):
            if i>0 and nums[i] == nums[i-1]:
                continue
            l =i+1
            r= len(nums)-1

            while l<r:
                sm = nums[i] + nums[l] + nums[r]

                if sm > 0:
                    r-=1
                elif sm <0:
                    l+=1
                else:
                    ans.append([nums[i], nums[l], nums[r]])
                    l+=1
                    while nums[l] == nums[l-1] and l<r:
                        l+=1

        return ans
                

        
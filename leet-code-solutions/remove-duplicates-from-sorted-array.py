class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        l=r=0
        count =0

        while r<len(nums):
            if nums[l] == nums[r]:
                r+=1
            else:
                if r-l > 1:
                    print('Y')
                    nums[l+1] , nums[r] = nums[r], nums[l+1]
                    count+=1
                    
                l+=1
                r+=1
        return len(set(nums))

        
        l= 0
        r = 1
        count = 1

        while r<len(nums):
            if nums[l] == nums[r]:
                nums.pop(r)
            elif nums[l] != nums[r]:
                count+=1
                l=r
                r=l+1
        print(nums)
        return count


            
        
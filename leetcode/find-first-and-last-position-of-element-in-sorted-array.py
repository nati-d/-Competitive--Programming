class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        left = -1
        right = len(nums)
        arr = []
        lft = 100000000
        rht = 0

        while left+1 < right:
            mid = (left + right) // 2
            
            if target == nums[mid]:
                lft = min(lft,mid)
                right = mid
            elif target > nums[mid]:
                left = mid
            else:
                right = mid
        
        left = -1
        right = len(nums)
        rht = 0
        
        while left+1 < right:
            mid = (left + right) // 2
            
            if target == nums[mid]:
                rht = max(rht,mid)
                left = mid
            elif target > nums[mid]:
                left = mid
            else:
                right = mid
        if lft == 100000000 and rht == 0:
            arr.append(-1)
            arr.append(-1)
            return arr
        # arr.append(lft)
        # arr.append(rht)
        # print(arr)
        # return arr
        print(lft,rht)
        arr.append(lft)
        arr.append(rht)
        return arr
        
        
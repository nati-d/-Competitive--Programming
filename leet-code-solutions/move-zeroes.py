class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        seek = 0
        place = 0

        while seek < len(nums):
            if nums[seek] !=0:
                nums[seek], nums[place] = nums[place], nums[seek]
                place+=1
            seek+=1


        
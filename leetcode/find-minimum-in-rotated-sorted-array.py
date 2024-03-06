from sortedcontainers import SortedList
class Solution:
    def findMin(self, nums: List[int]) -> int:
        nums = SortedList(nums)
        return min(nums)
        
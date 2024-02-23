class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        lst = nums+nums
        ans = []

        for i in range(len(nums)):
            mx = -1
            for j in range(i,len(lst)):
                if lst[j] > nums[i]:
                    mx = lst[j]
                    break
            ans.append(mx)
        return ans

        
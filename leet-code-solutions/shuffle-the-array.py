class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        arr1 =[]
        arr2 =[]
        result =[]
        for i in range(n):
            arr1.append(nums[i])
        for i in range(n,len(nums)):
            arr2.append(nums[i])

        for i in range(n):
            result.append(arr1[i])
            result.append(arr2[i])

        return result
        
class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        ans = []

        for i in range(len(arr2)):
            ct = arr1.count(arr2[i])
            ans.extend([arr2[i]] * ct)
        temp = []
        for i in range(len(arr1)):
            if arr1[i] not in ans:
                temp.append(arr1[i])
        temp.sort()
        ans.extend(temp)

        return ans
        
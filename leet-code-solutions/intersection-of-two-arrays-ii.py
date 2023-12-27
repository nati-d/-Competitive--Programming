class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        c1 = Counter(nums1)
        c2 = Counter(nums2)
        ans = []

        st = set(nums1).intersection(set(nums2))
        arr = list(st)

        for i in range(len(arr)):
            n = min(c1[arr[i]], c2[arr[i]])
            ans.extend([arr[i]]*n)
        return ans
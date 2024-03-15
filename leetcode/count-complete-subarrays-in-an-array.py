class Solution:
    def countCompleteSubarrays(self, nums: List[int]) -> int:
        distnict = set(nums)
        count = 0
        ln = len(distnict)
        n = len(nums)

        for i in range(n):
            dct = defaultdict(int)
            for j in range(i,n):
                dct[nums[j]] += 1
                if len(dct) > ln:
                    break
                elif len(dct) == ln:
                    count+=1
                
        return count



        
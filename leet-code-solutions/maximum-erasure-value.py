class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        N = len(nums)
        l = 0
        sm = nums[0]
        mx = max(0,sm)
        dct = Counter(nums[:1])
        print(dct,sm)

        for r in range(1,N):
            print('Y')
            dct[nums[r]] +=1
            sm+=nums[r]
            
            while dct[nums[r]] > 1:
                dct[nums[l]]-=1
                sm -= nums[l]
                l+=1

            
            r+=1
            mx = max(mx,sm)
        
        return mx


        
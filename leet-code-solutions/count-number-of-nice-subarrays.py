class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        N = len(nums)
        l = 0
        count = 0

        for c in range(N):
            if nums[c] % 2 == 0:
                nums[c] = 0
            else:
                nums[c] = 1
        print(nums)


        counter = {0:1}
        count = 0
        p_arr= [0]

        for i in range(len(nums)):
            p_arr.append(p_arr[i]+nums[i])
        
        print(p_arr)

        for right in range(1,len(p_arr)):
            nm = p_arr[right] - k
            if nm in counter:
                count+=counter[nm]
        
            if p_arr[right] in counter:
                counter[p_arr[right]] += 1
            else:
                counter[p_arr[right]] = 1
        return count


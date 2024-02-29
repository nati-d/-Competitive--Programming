class Solution:
    def getSumAbsoluteDifferences(self, nums: List[int]) -> List[int]:
        N =len(nums)
        prefix = [0] * N
        suffix = [0] * N
        smp = 0
        sms = 0
        for i in range(len(nums)):
            smp += nums[i]
            prefix[i] = smp
        for i in range(len(nums)-1,-1,-1):
            sms += nums[i]
            suffix[i] = sms
        print(prefix)
        print(suffix)
        ans = [0] * N

        for i in range(N):
            currentAbsoluteDiff = ((nums[i] * i) - prefix[i]) + (suffix[i] - (nums[i] * (N - i - 1)))
            ans[i] = currentAbsoluteDiff
        return ans
        
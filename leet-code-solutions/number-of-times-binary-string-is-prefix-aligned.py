class Solution:
    def numTimesAllBlue(self, flips: List[int]) -> int:
        mx = 0
        count = 0

        for i in range(len(flips)):
            mx = max(mx, flips[i]-1)
            if i == mx:
                count+=1
        return count



        n = len(flips)
        arr = [0] * n

        count =0

        for i in range(len(flips)):
            key = flips[i] - 1
            arr[key] = 1
            if 0 in arr[:i+1]:
                continue
            else:
                count+=1
        return count
        
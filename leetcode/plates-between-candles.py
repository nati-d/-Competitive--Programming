class Solution:
    def platesBetweenCandles(self, s: str, queries: List[List[int]]) -> List[int]:
        arr = []
        for c in s:
            if c == '*':
                arr.append(1)
            else:
                arr.append(0)
        for i in range(1,len(arr)):
            arr[i]+=arr[i-1]
        # # print(arr)
        # strt= 0
        # end=0
        candles = []
        for i in range(len(s)):
            if s[i] =='|':
                candles.append(i)
        print(candles)
        print(arr)
        ans = []
        for q in queries:
            if not candles:
                ans.append(0)
                continue
            if q[0] == q[1]:
                ans.append(0)
                continue
            left = bisect_left(candles,q[0])
            right = bisect_left(candles,q[1])
            if left > len(candles)-1:
                left-=1
            if right > len(candles)-1:
                right-=1
            elif candles[right] > q[1]:
                right-=1
            an = arr[candles[right]]-arr[candles[left]]
            if an >0:
                ans.append(an)
            else:
                ans.append(0)
            
        return ans
                
            

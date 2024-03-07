class Solution:
    def findRightInterval(self, intervals: List[List[int]]) -> List[int]:
        dic = defaultdict(int)
        ans = [-1]*len(intervals)

        for index,value in enumerate(intervals):
            dic[tuple(value)] = index
        
        intervals.sort()
        def checker(k,i):
            flag = False
            left = -1
            right = len(intervals)

            while left+1 < right:
                mid = (left+right)//2
                if intervals[mid][0] >= k[1]:
                    flag = True
                    right = mid
                else:
                    left = mid
            if flag:
                return intervals[right]
            else:
                return -1
            return right
        for index,value in enumerate(intervals):
            val = checker(value,index)
            if val == -1:
                ans[dic[tuple(value)]] = -1
            else:
                ans[dic[tuple(value)]] = dic[tuple(val)]
        return ans


            
                
                    
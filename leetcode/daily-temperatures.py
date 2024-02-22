class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        ans = [0]*n
        stack = []

        for i,t in enumerate(temperatures):
            while stack and temperatures[stack[-1]] < t:
                ans[stack[-1]] = i - stack[-1]
                stack.pop()
            stack.append(i)
        return ans

            
            

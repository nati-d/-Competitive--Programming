class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        n = len(arr)
        ans = 0
        
        nextSmaller = [n]*n
        prevSmaller = [n]*n
        stack = []

        for i,t in enumerate(arr):
            while stack and arr[stack[-1]] > t:
                nextSmaller[stack[-1]] = i - stack[-1]
                stack.pop()
            stack.append(i)
        
        for i in range(len(stack)):
            nextSmaller[stack[i]] -= stack[i]

        arr.reverse()
        stack = []
        for i,t in enumerate(arr):
            while stack and arr[stack[-1]] >= t:
                prevSmaller[stack[-1]] = i - stack[-1]
                stack.pop()
            stack.append(i)
        
        print(stack)
        for i in range(len(stack)):
            prevSmaller[stack[i]] -= stack[i]
        prevSmaller.reverse()
        print(prevSmaller)

        ans = 0

        arr.reverse()

        for i in range(len(nextSmaller)):
            ans += (nextSmaller[i]* prevSmaller[i] * arr[i])
        return ans % ( (10 ** 9) + 7)
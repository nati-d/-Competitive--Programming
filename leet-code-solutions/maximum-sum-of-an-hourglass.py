class Solution:
    def maxSum(self, grid: List[List[int]]) -> int:
        mx = 0
        arr = []
        for r in range(len(grid)-2):
            for c in range(len(grid[0])-2):
                temp = []
                for k in range(r, r+3):
                    for l in range(c, c+3):
                        temp.append(grid[k][l])
                arr.append(temp)
        mx = 0
        print(arr)
        for r in range(len(arr)):
            sm = sum(arr[r])
            sm -=(arr[r][3] + arr[r][5])
            mx = max(mx,sm)
        return mx
        return 3



n = int(input())
lst = list(map(int,input().split()))
memo = [0] * n
memo[1] = abs(lst[0] - lst[1])

for i in range(2,n):
    memo[i] = min(abs(lst[i] - lst[i-1]) + memo[i-1],abs(lst[i] - lst[i-2]) + memo[i-2])
print(memo[n-1])

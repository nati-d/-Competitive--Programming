n = int(input())
lst = list(map(int,input().split()))
lst.sort()
q = int(input())
days = []
for _ in range(q):
    days.append(int(input()))


for i in range(q):
    left = -1
    right = n
    ind = 0
    while left+1 < right:
        mid = (left+right)//2
        if lst[mid] > days[i]:
            right = mid
        else:
            ind = mid+1
            left = mid
    print(ind)


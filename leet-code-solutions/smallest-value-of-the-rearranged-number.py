class Solution:
    def smallestNumber(self, num: int) -> int:
        isNegative = False
        num = str(num)

        lst = list(num)
        if len(lst) == 1 and lst[0] == '0':
            return 0
        if lst[0] == '-':
            isNegative = True
        
        if isNegative:
            ans = []
            lst.sort(reverse = True)
            ans.extend(lst[:-1])
            a = ''.join(map(str,ans))
            return int(a)*(-1)

        else:
            lst.sort()
            z = lst.count('0')
            lst= [x for x in lst if x!='0']
            ans = []
            if z >= 1:
                ans.extend(lst[0])
                ans.extend([0]*z)
                ans.extend(lst[1:])
            else:
                ans.extend(lst)
            a = ''.join(map(str,ans))
            return int(a)
        
        
class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        skill.sort()
        N = len(skill)
        l = 0
        r = N-1
        lst = []
        flag = True
        sm = skill[l] + skill[r]
        ans = 0
        while l<r:
            lst.append([skill[l],skill[r]])
            l+=1
            r-=1
        print(lst)

        for i in range(len(lst)):
            print(sum(lst[i]))
            if sum(lst[i]) != sm:
                flag = False
                break
        if flag:
            for i in range(len(lst)):
                print(ans)
                ans += lst[i][0] * lst[i][1]
        else:
            return -1
        return ans
            



        
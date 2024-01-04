class Solution:
    def isPalindrome(self, s: str) -> bool:
        alp = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','0','1','2','3','4','5','6','7','8','9']
        st = []
        for i in range(len(s)):
            if s[i].lower() in alp:
                st.append(s[i].lower())
        N = len(st)
        l =0
        r = N-1
        flag = True

        while l<r:
            if st[l] != st[r]:
                flag = False
                break
                
            l+=1
            r-=1
        return flag


        
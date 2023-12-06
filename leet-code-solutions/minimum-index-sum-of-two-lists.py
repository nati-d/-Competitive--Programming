class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        # res=[]
        # s = inf
        # for i in range(len(list1)):
        #     if list1[i] in list2:
        #         sm = list1.index(list1[i])+ list2.index(list1[i])
        #         if  sm < s:
        #             s= sm
        #             res.append(list1[i])
        #         elif sm == s:
        #             res.append(list1[i])
        # return res
        d={}
        for i in range(len(list1)):
            for j in range(len(list2)):
                if list1[i] == list2[j]:
                    d[list1[i]] = i+j
        lst=[]
        for i,j in d.items():
            if j == min(d.values()):
                lst.append(i)
        return lst
            
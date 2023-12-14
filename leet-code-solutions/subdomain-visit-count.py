class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        result = []
        dic = defaultdict(int)
        c= cpdomains

        for i in range(len(c)):
            c[i] = list(c[i].split())

            
            c[i][1] = list(c[i][1].split("."))
            for j in range(len(c[i][1])):
                key = ".".join(c[i][1][j:])
                dic[key]+= int(c[i][0])

        for key, values in dic.items():
            s = str(values) + " " + key
            result.append(s)

        return result
        
                    

        
            
        
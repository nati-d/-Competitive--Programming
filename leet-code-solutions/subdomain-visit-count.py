class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        res = defaultdict(int)
        lastres = []
        for i in range(len(cpdomains)):
            inputo = cpdomains[i].split()
            inputo[0] = int(inputo[0])
            inputo[1] = inputo[1].split('.')
            print(inputo)

            for i in range(len(inputo[1])-1, -1, -1):
                # res[inputo[1][i]] += inputo[0]
                # if i != 0:
                #     inputo[1][i-1]+='.'+inputo[1][i]
               res[".".join(inputo[1][i:])]+=inputo[0]
               print(res)
        for key,val in res.items():
            lastres.append(str(val)+" "+key)
        return lastres
                    

        
            
        
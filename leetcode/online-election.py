class TopVotedCandidate:

    def __init__(self, persons: List[int], times: List[int]):
        self.persons = persons
        self.times = times

    def q(self, t: int) -> int:
        left = 0
        right = len(self.times)-1

        while left<=right:
            mid = (left+right)//2
            
            if self.times[mid] > t:
                right = mid-1
            else:
                left = mid+1
        dct = Counter(self.persons[:left])
        mxn = max(dct.values())
        mx = [self.persons[left-1], dct[self.persons[left-1]]]
        if mx[1] == mxn:
            return mx[0]
        visited = set()
        for i in range(left-1,-1,-1):
            if self.persons[i] not in visited and dct[self.persons[i]]>mx[1]:
                mx[0]=self.persons[i]
                mx[1] = dct[self.persons[i]]
                visited.add(self.persons[i])
                if mx[1] == mxn:
                    return mx[0]

        
        return mx[0]
        


# Your TopVotedCandidate object will be instantiated and called as such:
# obj = TopVotedCandidate(persons, times)
# param_1 = obj.q(t)
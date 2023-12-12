class Solution:
    def flipgame(self, fronts: List[int], backs: List[int]) -> int:
        doubles = {x for i, x in enumerate(fronts) if backs[i]==x}
        m = 3000
        for x in fronts+backs:
            if x not in doubles:
                m = min(m,x)
        return m if m!=3000 else 0
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        s = str(int("".join(map(str, digits))) + 1)
        return list(map(int, s))

        
class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        dct = Counter(answers)
        count = 0

        for key,values in dct.items():
            temp = ceil(values / (key+1 ))
            count += temp * (key+1)
        return count


        
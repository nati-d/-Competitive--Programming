class Solution:
    def predictTheWinner(self, nums: List[int]) -> bool:

        def winner (arr):
            if len(arr) ==1:
                return arr[0]
            if len(arr) == 2:
                return max(arr)
            first = arr[0]
            r1 = arr[2:]
            r2 = arr[1:-1]

            v1 = first + min(winner(r1),winner(r2))


            last = arr[-1]
            r1 = arr[1:-1]
            r2 = arr[:-2]

            v2 = last + min(winner(r1),winner(r2))

            return max(v1,v2)



        p1 = winner(nums)
        p2 = sum(nums) - p1
        return p1>=p2

        

        

        
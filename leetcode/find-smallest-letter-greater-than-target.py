class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        mn = "z"

        left = -1
        right = len(letters)
        flag = True

        while left+1 < right:
            mid = (left+right) //2
            if letters[mid] == target:
                left = mid
            elif letters[mid] < target:
                if letters[mid] > target:
                    flag = False
                    mn = min(mn,letters[mid])
                left = mid
            else :
                if letters[mid] > target:
                    flag = False
                    mn = min(mn,letters[mid])
                right = mid
        if flag:
            return letters[0]
        return mn

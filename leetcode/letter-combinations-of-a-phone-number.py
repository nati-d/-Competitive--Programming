class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        phone = {"2":"abc","3":'def',"4":"ghi","5":"jkl","6":"mno","7":"pqrs","8":"tuv","9":"wxyz"}
        ans = []
        bucket = []
        def backtrack(idx):
            if len(bucket) == len(digits):
                ans.append("".join(bucket.copy()))
                return
            
            for letter in phone[digits[idx]]:
                bucket.append(letter)
                backtrack(idx+1)
                bucket.pop()
        backtrack(0)
        if ans[0] == "":
            return []
        return ans
        
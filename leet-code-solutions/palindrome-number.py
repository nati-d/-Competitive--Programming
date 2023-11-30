class Solution:
    def isPalindrome(self, x: int) -> bool:
        x=str(x)
        arr1=[]
        for i in range(len(x)):
            arr1.append(x[i])
        arr1=arr1      
        rev = arr1[::-1]
        if arr1==rev:
            return True
        else:
            return False
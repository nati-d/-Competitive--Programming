# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        
        def sm(nd,sms):
            if not nd:
                return 0

            
            sms = sms*10+nd.val
            if not nd.left and not nd.right:
                return sms

            ls = sm(nd.left,sms) 
            rs = sm(nd.right,sms)
            return ls + rs
        
        return sm(root,0)

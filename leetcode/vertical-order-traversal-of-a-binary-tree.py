# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        dic = defaultdict(list)
        def tra(node,row,col):
            if not node:
                return []
            
            dic[(row,col)].append(node.val)
            
            ls = tra(node.left,row+1,col-1)
            rs = tra(node.right,row+1,col+1)

            return ls + rs

        tra(root,0,0)
        print(dic)
        d = dict(sorted(dic.items(), key = lambda x: (x[0][1],x[0][0])))

        other = defaultdict(list)
        ans = []
        for key,values in d.items():
            # if key[0] == key[1]:
            values.sort()
            other[key[1]].extend(values)
        for values in other.values():
            ans.append(values)
            
        print(d)

        
        return ans

class Solution:
    def simplifyPath(self, path: str) -> str:
        paths = list(map(str,path.split('/')))
        arr = []

        for c in paths:
            if c == ".":
                continue
            elif c =="..":
                if len(arr) > 0:
                    arr.pop()
                else:
                    continue
            elif c!= "":
                arr.append("/" + c)
        if len(arr) == 0:
            arr.append('/')
        return "".join(arr)

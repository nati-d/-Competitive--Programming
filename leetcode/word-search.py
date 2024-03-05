class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        visited = set()
        other = set()
        ans = []

        def backtrack(idx,row,col,visited):
            if idx >= len(word):
                return True
            if row>=len(board) or row < 0 or col < 0 or col>=len(board[0]):
                return False
            if (row,col) in visited:
                return False
            if board[row][col] != word[idx]:
                return False
            visited.add((row,col))
            return backtrack(idx+1,row+1,col,visited.copy()) or backtrack(idx+1,row,col+1,visited.copy()) or backtrack(idx+1,row,col-1,visited.copy()) or backtrack(idx+1,row-1,col,visited.copy())
                        
        
        for i in range(len(board)):
            for j in range(len(board[0])):
                visited = set()
                if board[i][j] == word[0] and backtrack(0,i,j, visited) :      
                    return True
        return False
    
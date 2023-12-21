class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
       
        for i in range(0,len(board)):
            data = set()
            for j in range(len(board)):
                if board[i][j] == '.':
                    continue
                if board[i][j] in data :
                    return False
                else:
                    data.add(board[i][j])
        for i in range(0,len(board)):
            data = set()
            for j in range(len(board)):
                if board[j][i] == '.':
                    continue
                if board[j][i] in data :
                    return False
                else:
                    data.add(board[j][i])

        for i in range(0,len(board), 3):
            for j in range(0,len(board),3):
                val = set()
                for k in range(i, i+3):
                    for y in range(j, j+3):

                        if board[k][y] == '.':
                            continue
                        if board[k][y] in val :
                            return False
                        else:
                            val.add(board[k][y])
                
            
            
        return True
            

        
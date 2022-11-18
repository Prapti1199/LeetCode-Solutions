class Solution:
    
    def solve(self, board):
        ch = ["1","2","3","4","5","6","7","8","9"]
        for i in range(0,len(board)):
            for j in range(0,len(board[0])):
                
                if board[i][j] == ".":
                    for c in ch:
                        if(self.isValid(board,i,j,c)):
                            board[i][j] = c
                            
                            if(self.solve(board) == True):
                                return True
                            else:
                                board[i][j] = "."
                    return False
                
        return True
    
    def isValid(self, board, row, col, ch):
        for i in range(0,9):
            if(board[i][col] == ch):
                return False
            if(board[row][i] == ch):
                return False
            if(board[3* int(row/3) + int(i/3)][3 * int(col/3) + int(i%3)] == ch):
                return False
        return True
            
    def solveSudoku(self, board: List[List[str]]) -> None:
        
        self.solve(board)
        """
        Do not return anything, modify board in-place instead.
        """
        
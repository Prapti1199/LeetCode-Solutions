class Solution:
   
    def solve(self, col, board, n, lowerDaigonal, upperDaigonal, leftRow):
        
        if(col == n):
            print(board)
            return 1
        
        ans = 0
        for r in range(0,n):
            if(leftRow[r] == 0 and lowerDaigonal[r+col] == 0 and upperDaigonal[n-1+col-r] == 0):
                board[r][col] = 'Q'
                leftRow[r] = 1
                lowerDaigonal[r+col] = 1
                upperDaigonal[n-1+col-r] = 1
                ans += self.solve(col+1,board, n, lowerDaigonal, upperDaigonal, leftRow)
                leftRow[r] = 0
                lowerDaigonal[r+col] = 0
                upperDaigonal[n-1+col-r] = 0
                board[r][col] = '.'
        return ans
    
    def totalNQueens(self, n: int) -> int:
        board = [['.']*n for i in range(n)]
        leftRow = [0 for i in range(n)]
        lowerDaigonal = [0 for i in range(2*n-1)]
        upperDaigonal = [0 for i in range(2*n-1)]
        
        return self.solve(0,board, n, lowerDaigonal, upperDaigonal, leftRow)
        
        
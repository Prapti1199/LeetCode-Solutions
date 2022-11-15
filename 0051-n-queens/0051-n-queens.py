class Solution:
    
  
    def solve(self, col, board, ans, n, lowerDaigonal, upperDaigonal, leftRow):
        
        if(col == n):
            print(board)
            ans.append(["".join(i) for i in board])
            return 
        
        for r in range(0,n):
            if(leftRow[r] == 0 and lowerDaigonal[r+col] == 0 and upperDaigonal[n-1+col-r] == 0):
                board[r][col] = 'Q'
                leftRow[r] = 1
                lowerDaigonal[r+col] = 1
                upperDaigonal[n-1+col-r] = 1
                self.solve(col+1,board,ans, n, lowerDaigonal, upperDaigonal, leftRow)
                leftRow[r] = 0
                lowerDaigonal[r+col] = 0
                upperDaigonal[n-1+col-r] = 0
                board[r][col] = '.'
    
    def solveNQueens(self, n: int) -> List[List[str]]:
        board = [['.']*n for i in range(n)]
        leftRow = [0 for i in range(n)]
        lowerDaigonal = [0 for i in range(2*n-1)]
        upperDaigonal = [0 for i in range(2*n-1)]
        ans = []
        
        self.solve(0,board, ans , n, lowerDaigonal, upperDaigonal, leftRow)
        return ans
        
        
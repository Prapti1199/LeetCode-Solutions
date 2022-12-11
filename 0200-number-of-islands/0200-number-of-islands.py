class Solution:
    
    def bfs(self, r, c, v, grid):
        v[r][c] = 1
        q = deque()
        q.append([r,c])
        nr = len(grid)
        nc = len(grid[0])
        while(q):
            s = q.pop()
            r = s[0]
            c = s[1]
             
            for row, col in ((-1,0), (1,0), (0,-1), (0,1)):
                    nrow = r + row
                    ncol = c + col
                    if nrow >= 0 and nrow <nr  and ncol >= 0 and ncol < nc and grid[nrow][ncol] == '1' and v[nrow][ncol] == 0:
                        
                        v[nrow][ncol] = 1
                        print("Inside : ", nrow, ncol, v[nrow][ncol])
                        q.append([nrow, ncol])
                        
                    
    def numIslands(self, grid: List[List[str]]) -> int:
        r = len(grid)
        c = len(grid[0])
        v = [[0 for i in range(c)] for j in range(r)]
        
        cnt = 0
        for i in range(0,r):
            for j in range(0,c):
                if (v[i][j] == 0 and grid[i][j] == '1'):
                    cnt = cnt + 1
                    self.bfs(i, j, v, grid)
                    
        return cnt
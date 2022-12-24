#User function Template for python3

from typing import List
from collections import deque

class Solution:    
    # def dfs(self, grid, i, j, visited):
    #     visited[i][j] = 1
        
    #     delta = [[-1,0], [0, -1], [1, 0], [0, 1]]
        
    #     for d in delta:
    #         nr = i + d[0]
    #         nc = j + d[1]
            
    #         if nr >= 0 and nr < n and nc >= 0 and nc < m and grid[nr][nc] == 'O' and visited[nr][nc] == 0:
    #             self.dfs(grid, nr, nc, visited)
      
    def bfs (self, grid, i, j, visited):
        visited[i][j] = 1
        queue = deque()
        
        queue.append([i,j])
        delta = [[-1,0], [0, -1], [1, 0], [0, 1]]
        
        while(queue):
            r, c = queue.popleft()
            for d in delta:
                nr = r + d[0]
                nc = c + d[1]
                if nr >= 0 and nr < n and nc >= 0 and nc < m and grid[nr][nc] == 1 and visited[nr][nc] == 0:
                    visited[nr][nc] = 1
                    queue.append([nr,nc])
            
      
    def numberOfEnclaves(self, grid: List[List[int]]) -> int:
        # code here
        n = len(grid)
        m = len(grid[0])
        visited = [[0 for i in range(m)] for j in range(n)]
        count = 0
 
        for i in range(n):
            for j in range(m):
                if (i == 0 or j == 0 or i == n-1 or j == m-1) and grid[i][j] == 1 and visited[i][j] == 0:
                    self.bfs(grid, i, j, visited)
                    
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1  and visited[i][j] == 0:
                    count += 1
                    
        return count

        


#{ 
 # Driver Code Starts
#Initial Template for Python 3


if __name__ == "__main__":
    for _ in range(int(input())):
        n, m = map(int,input().strip().split())
        grid = []
        for i in range(n):
            grid.append([int(i) for i in input().strip().split()])

        obj=Solution()
        print(obj.numberOfEnclaves(grid))
# } Driver Code Ends
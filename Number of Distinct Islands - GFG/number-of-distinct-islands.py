#User function Template for python3

import sys
from typing import List
sys.setrecursionlimit(10**8)
class Solution:
    
    def dfs(self, r, c, visited, grid, i, j, islands):
        n = len(grid)
        m = len(grid[0])
        visited[r][c] = 1
        islands.append([r - i, c - j])
        
        delta = [[0,1],[1,0],[0,-1],[-1,0]]
        
        for d in delta:
            nr = r + d[0]
            nc = c + d[1]
            
            if nr >= 0 and nr < n and nc >= 0 and nc < m and grid[nr][nc] == 1 and visited[nr][nc] == 0:
                self.dfs(nr, nc, visited, grid, i, j, islands)
        
    
    def countDistinctIslands(self, grid : List[List[int]]) -> int:
        # code here
        r = len(grid)
        c = len(grid[0])
        visited = [[0 for i in range(c)] for j in range(r)]
        unique_set = set()
        
        for i in range(r):
            for j in range(c):
                if visited[i][j] == 0 and grid[i][j] == 1:
                    islands = []
                    self.dfs(i,j,visited,grid,i,j,islands)
                    unique_set.add(tuple(tuple(map(tuple,islands))))
                    
        return len(unique_set)
        


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__=="__main__":
    for _ in range(int(input())):
        n,m=map(int,input().strip().split())
        grid=[]
        for i in range(n):
            grid.append([int(i) for i in input().strip().split()])
        obj=Solution()
        print(obj.countDistinctIslands(grid))
# } Driver Code Ends
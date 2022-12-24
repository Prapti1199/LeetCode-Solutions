#User function Template for python3

class Solution:
    
    def dfs(self, mat, i, j, visited):
        visited[i][j] = 1
        
        delta = [[-1,0], [0, -1], [1, 0], [0, 1]]
        
        for d in delta:
            nr = i + d[0]
            nc = j + d[1]
            
            if nr >= 0 and nr < n and nc >= 0 and nc < m and mat[nr][nc] == 'O' and visited[nr][nc] == 0:
                self.dfs(mat, nr, nc, visited)
    
    def fill(self, n, m, mat):
        # code here
        visited = [[0 for i in range(m)] for j in range(n)]
        ans = mat
        
        for i in range(n):
            for j in range(m):
                if (i == 0 or j == 0 or i == n-1 or j == m-1) and mat[i][j] == 'O' and visited[i][j] == 0:
                    self.dfs(mat, i, j, visited)
                    
        for i in range(n):
            for j in range(m):
                if mat[i][j] == 'O' and visited[i][j] == 0:
                    ans[i][j] = 'X'
                    
        return ans


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n, m = [int(x) for x in input().split()]
        mat = []
        for i in range(n):
            s = list(map(str,input().split()))
            mat.append(s)
        
        ob = Solution()
        ans = ob.fill(n, m, mat)
        for i in range(n):
            for j in range(m):
                print(ans[i][j], end = " ")
            print()
# } Driver Code Ends
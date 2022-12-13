class Solution:

    #Function to find minimum time required to rot all oranges. 
	def orangesRotting(self, grid):
		#Code here
		n = len(grid)
		m = len(grid[0])
		v = [[0 for i in range(m)] for j in range(n)]
		queue = []
		cntf = 0
		cnt = 0
		
		for i in range(0,n):
		    for j in range(0,m):
		        if grid[i][j] == 2:
		            queue.append([i,j, 0])
		            v[i][j] = 2
		            
		        if grid[i][j] == 1:
		            cntf += 1
		t = 0
		while(queue):
		    s = queue.pop(0)
            r = s[0]
            c = s[1]
            l = s[2]
            t = max(t,l)
            delta = [[-1,0], [0,-1], [1,0], [0,1]]
            
            for i in delta:
                nrow = r + i[0]
                ncol = c + i[1]
                if nrow >= 0 and nrow < n and ncol >= 0 and ncol < m and grid[nrow][ncol] == 1 and v[nrow][ncol] == 0 :
                    v[nrow][ncol] = 2
                    queue.append([nrow, ncol, l+1])
                    cnt += 1
        
        if cnt != cntf:
            return -1
        else:
            return t
		            


#{ 
 # Driver Code Starts
from queue import Queue

if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		n, m = map(int, input().split())
		grid = []
		for _ in range(n):
			a = list(map(int, input().split()))
			grid.append(a)
		obj = Solution()
		ans = obj.orangesRotting(grid)
		print(ans)

# } Driver Code Ends
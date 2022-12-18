from collections import deque

class Solution:

    #Function to find distance of nearest 1 in the grid for each cell.
	def nearest(self, grid):
		#Code here
		row = len(grid)
		col = len(grid[0])
		
		visited = [[0 for i in range(col)] for j in range(row)]
		distance = [[0 for i in range(col)] for j in range(row)]
		d = [[0,-1], [-1,0], [0,1], [1,0]]
		
		
		queue = deque()
		
		for i in range(row):
		    for j in range(col):
		        if grid[i][j] == 1:
		            queue.append((i,j,0))
		            visited[i][j] = 1
        while queue:
            r,c,dist = queue.popleft()
            distance[r][c] = dist
            for i in d:
                newr = r + i[0]
                newc = c + i[1]
                if newr >= 0 and newr < row and newc >= 0 and newc < col and visited[newr][newc] == 0:
                    visited[newr][newc] = 1
                    queue.append((newr, newc, dist+1))
        return distance


#{ 
 # Driver Code Starts
if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		n, m = map(int, input().split())
		grid = []
		for _ in range(n):
			a = list(map(int, input().split()))
			grid.append(a)
		obj = Solution()
		ans = obj.nearest(grid)
		for i in ans:
			for j in i:
				print(j, end = " ")
			print()

# } Driver Code Ends
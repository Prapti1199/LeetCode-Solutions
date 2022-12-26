from collections import deque

class Solution:
    
    def bfs(self, start, V, adj, color):
        queue = deque()
        queue.append(start)
        color[start] = 0
        
        while(queue):
            s = queue.popleft()
            for i in adj[s]:
                if color[i] == -1:
                    color[i] = 1 - color[s]
                    queue.append(i)
                
                elif color[i] == color[s]:
                    return False
        
        return True
        
	def isBipartite(self, V, adj):
		#code here
		color = [-1 for i in range(V)]
		
		for i in range(V):
		    if color[i] == -1:
		        if(self.bfs(i, V, adj, color) == False):
		            return False
		
		return True


#{ 
 # Driver Code Starts
if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		V, E = map(int, input().strip().split())
		adj = [[] for i in range(V)]
		for i in range(E):
			u, v = map(int, input().strip().split())
			adj[u].append(v)
			adj[v].append(u)
		obj = Solution()
		ans = obj.isBipartite(V, adj)
		if(ans):
			print("1")
		else:
			print("0")

# } Driver Code Ends
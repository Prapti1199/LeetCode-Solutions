#User function Template for python3


class Solution:
    
    def dfs(self, adj, V, start, visited):
        visited[start] = 2
        
        for s in adj[start]:
            if visited[s] == 0:
               if self.dfs(adj, V, s, visited):
                    return True
            
            elif visited[s] == 2:
                return True
        
        visited[start]= 1
        return False
    
    #Function to detect cycle in a directed graph.
    def isCyclic(self, V, adj):
        # code here
        visited = [0 for i in range(V)]
        for i in range(V):
            if visited[i] == 0:
                if self.dfs(adj, V, i, visited):
                    return True
                    
        return False

#{ 
 # Driver Code Starts
#Initial Template for Python 3

import sys
sys.setrecursionlimit(10**6)
        
if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        V,E = list(map(int, input().strip().split()))
        adj = [[] for i in range(V)]
        for i in range(E):
            a,b = map(int,input().strip().split())
            adj[a].append(b)
        ob = Solution()
        
        if ob.isCyclic(V, adj):
            print(1)
        else:
            print(0)
# } Driver Code Ends
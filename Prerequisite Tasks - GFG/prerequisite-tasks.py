#User function Template for python3
from collections import deque

class Solution:
    def isPossible(self,N,prerequisites):
        #code here
        adj = [[] for i in range(N)]
        indegree = [0 for i in range(N)]
        queue = deque()
        count = 0
        for i in prerequisites:
            adj[i[0]].append(i[1])
            
        for n in range(N):
            for a in adj[n]:
                indegree[a] = indegree[a] + 1
        
        for n in range(N):
            if indegree[n] == 0:
                queue.append(n)
                
        while(queue):
            node = queue.popleft()
            count += 1
            
            for i in adj[node]:
                indegree[i] -= 1
                if indegree[i] == 0:
                    queue.append(i)
            
        if count == N:
            return True
        else:
            False
            


#{ 
 # Driver Code Starts
#Initial Template for Python 3
if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases) :
        N=int(input())
        P=int(input())

        prerequisites=[]
        for _ in range(P):
            pair = [int(x) for x in input().split()]
            prerequisites.append(pair)
        ob=Solution()
        if(ob.isPossible(N,prerequisites)):
            print("Yes")
        else:
            print("No")
# } Driver Code Ends
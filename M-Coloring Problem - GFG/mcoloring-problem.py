

def graphColoring(graph, k, V):
    
    def possible(graph, vertex, color, col, V):
        for i in range(V):
            if graph[vertex][i] and color[i] == col:
                return False
        return True
    
    def colorG(vertex, graph, k, V, color):
        if vertex == V:
            return True
        
        for col in range(k):
            if possible(graph, vertex, color, col+1, V):
                color[vertex] = col+1
                if colorG(vertex+1, graph, k, V, color):
                    return True
                color[vertex] = 0
        return False

    color = [0]*V
    return colorG(0, graph, k, V, color)
    
    #your code here
   
 #your code here


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == "__main__":
    t = int(input())
    while(t>0):
        V = int(input())
        k = int(input())
        m = int(input())
        list = [int(x) for x in input().strip().split()]
        graph = [[0 for i in range(V)] for j in range(V)]
        cnt = 0
        for i in range(m):
            graph[list[cnt]-1][list[cnt+1]-1]=1
            graph[list[cnt+1]-1][list[cnt]-1]=1
            cnt+=2
        if(graphColoring(graph, k, V)==True):
            print(1)
        else:
            print(0)

        t = t-1

# } Driver Code Ends
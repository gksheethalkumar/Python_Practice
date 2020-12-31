import collections
class Solution:
    def networkDelayTime(self, times, N, K):
        ## N is number of Nodes
        ## K is the starting Node
        ## We need to find the shortest path from K 
        
        #1 Create a graph from times in [[Source [Dest, distance]]]
        
        graph = collections.defaultdict(list)
        for u,v,w in times:
            graph[u].append([v,w])
        
        
        
        ## 2 Set distance to all nodes as infinity
        
        dist = {node: float('inf') for node in range(1,N+1)}
        
        ## Set distance to K node as 0
        
        dist[K] = 0
        ## 3 Create an empty list to mark self.seen elements
        self.seen = [False] * (N+1)
        
        ## Remember path
        parent = [-1] * (N+1)
        ### 4 Main dijkstras logic
        
        while True:
            
            current_node = -1
            current_distance = float('inf')
            
            ## get the node that we need to work ok, that is current node.
            ## make sure it is not self.seen
            for n in range(1,N+1):
                if self.seen[n] is False and dist[n] < current_distance:
                    current_distance = dist[n]
                    current_node = n
                    
            
            ## base case to break loop when all nodes are self.seen
            if current_node  == -1: 
                break
            self.seen[current_node] = True
            ### Actual Algo : 
            
            
            for nei, distance in graph[current_node]:
                dist[nei] = min(dist[nei],dist[current_node] + distance)
                parent[nei] = current_node

        #return max(dist.values()) if max(dist.values()) < float('inf') else -1
        self.printSolution(dist, parent,K)

    def printSolution(self, dist, parent,K): 
            src = K
            print("Vertex \t\tDistance from Source\tPath") 
            for i in range(1, len(dist)): 
                print("\n%d --> %d \t%d \t" % (src, i, dist[i])), 
                self.printPath(parent,i) 
        

    def printPath(self, parent, j): 
          
        #Base Case : If j is source 
        if parent[j] == -1 :  
            print (j), 
            return
        self.printPath(parent , parent[j]) 
        print (j),         

                
                
a = Solution()
l = [[2,1,1],[2,3,1],[3,4,1]]
print(a.networkDelayTime(l,4,2))


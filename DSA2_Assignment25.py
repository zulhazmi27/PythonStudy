#Prim's Algorithm with MST

class Graph():
    def __init__(self, vertices):
        self.v = vertices
        self.graph = [[0 for column in range(vertices)] 
                      for row in range(vertices)] #initialise graph with 0s
    
    def printMST(self, parent):
        print("Edge \tWeight")
        for i in range(1, self.v):
            print(parent[i], "-", i, "\t", self.graph[i][parent[i]]) #print the MST
            
    def minKey(self, key, mstSet):
        min = float('inf') #set min to infinity
        
        for v in range(self.v): #find the minimum key value from the set of vertices not yet included in MST
            if key[v] < min and mstSet[v] == False:
                min = key[v]
                min_index = v

        return min_index
    
    def primMST(self):
        key = [float('inf')] * self.v #Key values used to pick minimum weight edge in cut 
        parent = [None] * self.v  #Array to store constructed MST
        
        key[0] = 0 #Make key 0 so that this vertex is picked as first vertex    
        mstSet = [False] * self.v   
        
        parent[0] = -1 #First node is always the root of MST
        
        for i in range(self.v):
            u = self.minKey(key, mstSet) #Pick the minimum key vertex from the set of vertices not yet included in MST
            
            mstSet[u] = True #Add the picked vertex to the MST Set
            
            for v in range(self.v): #Update key value and parent index of the adjacent vertices of the picked vertex. Consider only those vertices which are not yet included in MST
                if self.graph[u][v] > 0 and mstSet[v] == False and key[v] > self.graph[u][v]:
                    key[v] = self.graph[u][v]
                    parent[v] = u
        
        self.printMST(parent)
        

g = Graph(12) #create a graph with n vertices
g.graph = [[0, 3, 5, 4, 0, 0, 0, 0, 0, 0, 0, 0],
           [3, 0, 0, 0, 3, 6, 0, 0, 0, 0, 0, 0],
           [5, 0, 0, 2, 0, 0, 4, 0, 0, 0, 0, 0],
           [4, 0, 2, 0, 1, 0, 0, 5, 0, 0, 0, 0],
           [0, 3, 0, 1, 0, 2, 0, 0, 4, 0, 0, 0],
           [0, 6, 0, 0, 2, 0, 0, 0, 0, 5, 0, 0],
           [0, 0, 4, 0, 0, 0, 0, 3, 0, 0, 6, 0],
           [0, 0, 0, 5, 0, 0, 3, 0, 6, 0, 7, 0],
           [0, 0, 0, 0, 4, 0, 0, 6, 0, 3, 0, 5],
           [0, 0, 0, 0, 0, 5, 0, 0, 3, 0, 0, 9],
           [0, 0, 0, 0, 0, 0, 6, 7, 0, 0, 0, 8],
           [0, 0, 0, 0, 0, 0, 0, 0, 5, 9, 8, 0]]

g.primMST()
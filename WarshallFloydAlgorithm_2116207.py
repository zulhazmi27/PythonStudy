#Write a code for Warshall-Floyd algorithm. Input the graph from Assignment 21 and compare your output with your answer in Assignment 21.

from collections import defaultdict
 
#Class to represent a graph
class Graph:
 
    def __init__(self, vertices):
        self.V = vertices
 
    # A utility function to print the solution
    def printSolution(self, reach):
        print ("Following matrix transitive closure of the given graph ")   
        for i in range(self.V):
            for j in range(self.V):
                if (i == j):
                  print ("%7d\t" % (1),end=" ")
                else:
                  print ("%7d\t" %(reach[i][j]),end=" ")
            print()
     
     
    # Prints transitive closure of graph[][] using Floyd Warshall algorithm
    def transitiveClosure(self,graph):

        reach = [i[:] for i in graph]

        for k in range(self.V):
            for i in range(self.V):
                for j in range(self.V):

                    reach[i][j] = reach[i][j] or (reach[i][k] and reach[k][j])
 
        self.printSolution(reach)
         
g= Graph(6)
 
graph = [[0, 1, 0, 1, 0, 0],
         [0, 0, 0, 0, 1, 0],
         [0, 0, 0, 0, 1, 1],
         [0, 1, 0, 0, 0, 0],
         [0, 0, 0, 1, 0, 0],
         [0, 0, 0, 0, 0, 1]]
 
g.transitiveClosure(graph)
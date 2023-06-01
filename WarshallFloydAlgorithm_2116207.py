#Write a code for Warshall-Floyd algorithm. Input the graph from Assignment 21 and compare your output with your answer in Assignment 21.

v = 4 #number of vertices
inf = 99999 #infinity used to represent no path between two vertices

graph = [
        [0, 5, inf, 10],
        [inf, 0, 3, inf],
        [inf, inf, 0,   1],
        [inf, inf, inf, 0]
        ] #graph represented as a 2D list


def floydWarshall(graph): #function to implement Warshall-Floyd algorithm
    dist = list(map(lambda i: list(map(lambda j: j, i)), graph)) #create a copy of the graph
    
    for k in range(v): #iterate through all vertices as source
        for i in range(v): #iterate through all vertices as destination
            for j in range(v): #iterate through all vertices as intermediate
                dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j]) #update the distance between i and j if there is a shorter path through k

    displaySolution(dist) #display the solution

def displaySolution(dist): 
    print("Matrix of minimal distances :")
    
    for i in range(v):#iterate through all vertices as source
        for j in range(v): #iterate through all vertices as destination
            if(dist[i][j] == inf):
                print("%7s" % ("inf"), end = " ") #print inf if there is no path between i and j
            else:
                print("%7d\t" % (dist[i][j]), end = "") #print the distance between i and j
            
            if j == v - 1: #print a new line if all vertices as destination have been iterated through
                print()

floydWarshall(graph)

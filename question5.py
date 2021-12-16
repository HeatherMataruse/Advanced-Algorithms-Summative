#by Heather Mataruse


from collections import defaultdict
import heapq
#here is the direction in which we move from 1 going to different  nodes
edges = [[1,2,24],[1,4,20],[3,1,3],[4,3,12]]


def tree_matrix(edges): # for this function I am creating the graph I am going to use 
    my_graph = {x:[] for x in range(1,len(edges)+1)}
    for i,j,k in edges:
        if i not in my_graph or j not in my_graph:
            my_graph[i] = (j,k)
            my_graph[j] = (i,k)
        else:
            my_graph[i].append((j,k))
            my_graph[j].append((i,k))
    return my_graph   
#in the shortestReach function we have  n which is the total number of nodes in the graph
# edges as the total number of edges we have 
#s which is our starting point to travel in the graph
def shortestReach(s,n,edges):
    my_heap = [(0, s)]
    my_graph = tree_matrix(edges)
    list_   = {}
    for i in range(1, n + 1):
        list_ [i] = float('inf')
    list_ [s] = 0
    while my_heap:
        v = heapq.heappop(my_heap)
        for e in my_graph[t[1]]:
            if list_ [e[0]] > list_ [v[1]] + e[1]:
               list_ [e[0]] = list_ [v[1]] + e[1]
             
                if (e[1], e[0]) in my_heap:
                    my_heap.remove((e[1], e[0]))
                    heapq.heapify(my_heap)
                
                heapq.heappush(my_heap, (list_ [e[0]], e[0]))
            
    shortest_reach = [] #this is the list that is going to store the  
    # n - 1 integers denoting the shortest distance to the n - 1 nodes from starting position s

    for i in list_ :
        shortest_reach.append(list_ [i])

    return shortest_reach[1:]

s = 1 #s is where we are starting which is node 1
print("The Shortest Distance is " , shortestReach(len(edges),edges,s))

#by Heather Mataruse


from collections import defaultdict
import heapq
#here is the direction in which we move from 1 going to different  nodes
edges = [[1,2,24],[1,4,20],[3,1,3],[4,3,12]]


def compose_graph(edges): # for this function I am creating the graph I am going to use 
    my_graph = {x:[] for x in range(1,len(edges)+1)}
    for a,b,c in edges:
        if a not in my_graph or b not in my_graph:
            my_graph[a] = (b,c)
            my_graph[b] = (a,c)
        else:
            my_graph[a].append((b,c))
            my_graph[b].append((a,c))
    return my_graph   
#in the shortestReach function we have  n which is the total number of nodes in the graph
# edges as the total number of edges we have 
#s which is our starting point to travel in the graph
def shortestReach(n,edges,s):
    my_heap = [(0, s)]
    my_graph = compose_graph(edges)
    answer    = {}
    for a in range(1, n + 1):
        answer[a] = float('inf')
    answer[s] = 0
    while my_heap:
        t = heapq.heappop(my_heap)
        for h in my_graph[t[1]]:
            if answer[h[0]] > answer[t[1]] + h[1]:
                answer[h[0]] = answer[t[1]] + h[1]
             
                if (h[1], h[0]) in my_heap:
                    my_heap.remove((h[1], h[0]))
                    heapq.heapify(my_heap)
                
                heapq.heappush(my_heap, (answer[h[0]], h[0]))
            
    shortest_reach = [] #this is the list that is going to store the  
    # n - 1 integers denoting the shortest distance to the n - 1 nodes from starting position s

    for i in answer:
        shortest_reach.append(answer[i])

    return shortest_reach[1:]

s = 1 #s is where we are starting which is node 1
print("The Shortest Distance is " , shortestReach(len(edges),edges,s))

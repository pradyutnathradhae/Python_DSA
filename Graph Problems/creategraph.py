import math
# class node:
#     def __init__(self,root) -> None:
#         self.nodeval = root
        
class Graph:
    def __init__(self,graph_dict) -> None:
        self.graphdict = graph_dict
    # def neighbours 

def creategraph():
    graph = {}
    n = int(input('Enter no. of vertices:'))
    for i in range(n):
        temp = list(map(int,input().split()))
        val = temp[0]
        graph[val] = temp[1:]
    return graph

def creategraph_with_wts(n):
    
    graph = [[math.inf for j in range(n)] for i in range(n)]
    e = int(input("Enter the no. of edges"))
    print("Enter the src,dest,edge weight of edges")
    for i in range(e):
        
        src,dest,val = map(int,input().split())
        if graph[src][dest] > val:
            graph[src][dest] = val
            graph[dest][src] = val
    return graph
            
    
    return graph

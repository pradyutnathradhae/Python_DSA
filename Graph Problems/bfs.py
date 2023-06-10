# from creategraph import Graph

def creategraph():
    graph = {}
    n = int(input('Enter no. of vertices:'))
    for i in range(n):
        temp = list(map(int,input().split()))
        val = temp[0]
        graph[val] = temp[1:]
    return graph

def bfs_traversal(graph,visited,val,queue):
    print(val)
    visited[val] = 1
    queue.pop(0)
    if len(graph[val]) == 0:
        return
    elif len(graph[val]) != 0:
        for i in graph[val]:
            if visited[i] == 0:
                queue.append(i)
    if len(queue) == 0:
        return
    else:
        bfs_traversal(graph,visited,queue[0],queue)
        
if __name__ == '__main__':
    graph = creategraph()
    visited = {}
    for i in graph:
        visited[i] = 0
    start = int(input('Enter Start Node:'))
    bfs_traversal(graph,visited,start,[start])
            
        
        
def creategraph():
    graph = {}
    n = int(input('Enter no. of vertices:'))
    for i in range(n):
        temp = list(map(int,input().split()))
        val = temp[0]
        graph[val] = temp[1:]
    return graph

def dfs_traversal(graph,visited,val,stack):
    print(val)
    visited[val] = 1
    stack.pop(-1)
    for i in graph[val]:
            if visited[i] == 0:
                stack.append(i)
                dfs_traversal(graph,visited,stack[-1],stack)
    if len(stack) == 0:
        return
        
if __name__ == '__main__':
    graph = creategraph()
    visited = {}
    for i in graph:
        visited[i] = 0
    start = int(input('Enter Start Node:'))
    dfs_traversal(graph,visited,start,[start])
            
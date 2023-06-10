from creategraph import creategraph_with_wts
import math

def find_neighbors(arr):
    temp = set()
    for i in range(len(arr)):
        if arr[i] != math.inf:
            temp.add(i)
    return temp

def find_notadded(mst,n):
    temp = []
    for i in range(n):
        if i not in mst:
            temp.append(i)
    return temp

n = int(input('Enter no. of vertices:'))
finalmst = []
graph = creategraph_with_wts(n)
mstset = set()
# mstset.add(0)
keyvalue = [math.inf]*n
keyvalue[0] = 0
while len(mstset) != n:
    notadded = find_notadded(mstset,n)
    temp = [keyvalue[i] for i in notadded]
    u = notadded[temp.index(min(temp))]
    mstset.add(u)
    neigh = find_neighbors(graph[u])
    for v in neigh:
        if graph[u][v] < keyvalue[v] :
            if (v,u) not in finalmst:
                finalmst.append((u,v))
                keyvalue[v] = graph[u][v]

print("The MST edges are:\n")
cost = 0
for i in finalmst:
    cost += graph[i[0]][i[1]]
    print('{} -> {}'.format(i[0],i[1]))
print('Cost of MST - > ',cost)        
    # minind = keyvalue.index(min(mstset))
    # neigh = find_neighbors(graph[minind])
    # neighwt = [graph[minind][i] for i in neigh]
    # minneigh = neighwt.index(min(neighwt))
    # neigh[minneigh]
    
            
    
    
    
    



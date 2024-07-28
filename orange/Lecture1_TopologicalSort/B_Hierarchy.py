'''
Hierarchy


'''

import queue

def topoSort(graph, result):
    V = len(graph)
    indegeree = [0] * V
    zero_indegree = queue.Queue()
    for u in range(V):
        for v in graph[u]:
            indegeree[v] += 1
    for i in range(V):
        if indegeree[i] == 0:
            zero_indegree.put(i)
    while not zero_indegree.empty():
        u = zero_indegree.get()
        result.append(u)
        for v in graph[u]:
            indegeree[v] -= 1
            if indegeree[v] == 0:
                zero_indegree.put(v)
    return len(result) == V


N, K = map(int, input().split())
graph = [[] for _ in range(N+1)]
result = []
for u in range(1,K+1):
    mylist = list(map(int, input().split()))
    W = mylist[0]
    V_list = mylist[1:]
    for v in V_list:
        graph[u].append(v)

topoSort(graph, result)
print(result[1:])


import queue

n, m = map(int, input().split())
#arr_cats store the positions of cats
arr_cats = list(map(int, input().split())) #remember to -1 when use this array because graph's node starts with 1
M = 10**5
G = [[] for _ in range(M+3)]
for _ in range(n-1):
    u, v = map(int, input().split())
    G[u].append(v)
    G[v].append(u)

def BFS(arr_cats, G):
    num_cats = [0]*(M+3) #stores number of cats that we passed in the way
    visited = [False]*(M+3)
    dist = [-1]*(M+3)

    num_cats[1] = arr_cats[1-1]
    visited[1] = True
    dist[1] = 0

    q = queue.Queue()
    q.put(1)
    count = 0
    while not q.empty():
        u = q.get()
        for v in G[u]:
            if not visited[v] and num_cats[u] <= m:
                visited[v] = True
                if arr_cats[v-1] != 0:
                    num_cat_v = num_cats[u] + arr_cats[v-1]
                    num_cats[v] = num_cat_v
                dist[v] = dist[u] + 1
                q.put(v)

                if len(G[v]) == 1 and num_cats[v] <= m: # length of adjacency list of node equals 1 means that the node is a leaf
                    count += 1
    return count

count = BFS(arr_cats, G)
print(count)
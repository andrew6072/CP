import queue

def BFS(G, visited, path, s):
    visited[s] = True
    q = queue.Queue()
    q.put(s)
    while not q.empty():
        u = q.get()
        for v in G[u]:
            if not visited[v]:
                path[v] = u
                q.put(v)
                visited[v] = True

def Solve(m, n, maze):
    G = [[] for _ in range(m * n + 3)]
    num_vertex = 0
    # array gate_i gate_j stores '.' that are in bounds i=0 j=0 i=n j=m
    gate_i = []
    gate_j = []
    #convert maze into adjacency list of a graph:
    # horizontal: 1 2 3 4 5 ... j ... m
    # vertical: 1 2 3 4 5 ... i ... n
    # each '.' in maze is a node in graph
    for i in range(n):
        for j in range(m):
            if maze[i][j] == '.':
                u = i * m + j + 1
                if i >= 1:
                    if maze[i-1][j] == '.':
                        v = (i-1) * m + j + 1
                        G[u].append(v)
                if j >= 1:
                    if maze[i][j-1] == '.':
                        v = i * m + j
                        G[u].append(v)
                if j <= m-2:
                    if maze[i][j+1] == '.':
                        v = i * m + j + 2
                        G[u].append(v)
                if i <= n-2:
                    if maze[i+1][j] == '.':
                        v = (i + 1) * m + j + 1
                        G[u].append(v)

                num_vertex += 1

                if i == 0 or j == 0 or i == n-1 or j == m-1:
                    gate_i.append(i)
                    gate_j.append(j)

    if len(gate_j) != 2 or num_vertex == 0 or (n == 1 and m == 1):
        print('invalid')
    else:
        s = gate_i[0] * m + gate_j[0] + 1
        f = gate_i[1] * m + gate_j[1] + 1
        path = [-1] * (n * m + 3)
        visited = [False] * (n * m + 3)
        BFS(G, visited, path, s)
        if path[f] == -1:
            print('invalid')
        else:
            print('valid')

t = int(input())
while t > 0:
    n, m = map(int, input().split())
    maze = []
    for i in range(n):
        ele_maze = input()
        maze.append(ele_maze)
    Solve(m, n, maze)
    t -= 1
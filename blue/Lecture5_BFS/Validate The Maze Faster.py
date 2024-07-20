import queue

dRow = [-1, 0, 1, 0]
dCol = [0, 1, 0, -1]

def IsValid(m, n, maze, visited, row, col):
    if row < 0 or col < 0 or row >= n or col >= m:
        return False
    if visited[row][col] == True:
        return False
    if maze[row][col] != '.':
        return False
    return True

def BFS(m, n, maze, row, col):
    visited = [[ False for _ in range(m)] for _ in range(n)]
    q = queue.Queue()
    q.put((row, col))
    visited[row][col] = True
    out_gates = []
    while not q.empty():
        cell = q.get()
        x = cell[0]
        y = cell[1]
        for i in range(4):
            adjx = x + dRow[i]
            adjy = y + dCol[i]
            if IsValid(m, n, maze, visited, adjx, adjy):
                q.put((adjx, adjy))
                visited[adjx][adjy] = True
                if adjx == 0 or adjx == n-1 or adjy == 0 or adjy == m-1:
                    out_gates.append((adjx, adjy))
    return out_gates

def Solve(m,n,maze):
    if m == 1 and n == 1:
        print('invalid')
        return
    count = 0
    gates = []
    for j in range(m):
        if maze[0][j] == '.' :
            gates.append((0,j))
            count += 1
        if maze[n-1][j] == '.' and n-1 != 0:
            gates.append((n-1,j))
            count += 1

    for i in range(1, n-1):
        if maze[i][0] == '.' :
            gates.append((i, 0))
            count += 1
        if maze[i][m-1] == '.' and m-1 != 0:
            gates.append((i, m-1))
            count += 1

    if count == 2:
        in_cell = gates[0]
        out_gate = BFS(m,n,maze,in_cell[0], in_cell[1])
        if len(out_gate) == 1:
            if out_gate[0] == gates[1]:
                print('valid')
        else:
            print('invalid')
    else:
        print('invalid')

t = int(input())
while t > 0:
    n, m = map(int, input().split())
    maze = []
    for i in range(n):
        ele_maze = input()
        maze.append(ele_maze)
    #print(BFS(m, n, maze, 0, 1))
    Solve(m,n,maze)
    t -= 1

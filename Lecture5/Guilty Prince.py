import queue

dRow = [-1, 0, 1, 0]
dCol = [0, 1, 0, -1]

def findStartPoint(m, n, maze):
    row = -1
    col = -1
    for i in range(n):
        for j in range(m):
            if maze[i][j] == '@':
                row = i
                col = j
    return (row, col)

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
    count = 1
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
                count += 1
    return count

def Solve(m, n, maze):
    start_point = findStartPoint(m, n, maze)
    count = BFS(m,n,maze,start_point[0], start_point[1])
    print(count)

t = int(input())
tc = 1
while t > 0:
    m, n = map(int, input().split())
    maze = []
    for i in range(n):
        ele_maze = input()
        maze.append(ele_maze)
    print(f'Case {tc}:', end=' ')
    Solve(m,n,maze)
    tc += 1
    t -= 1
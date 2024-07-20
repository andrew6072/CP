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

def BFS(m, n, maze, dist, row, col):
    visited = [[False for _ in range(m)] for _ in range(n)]
    q = queue.Queue()
    q.put((row, col))
    visited[row][col] = True
    dist[row][col] = 0

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
                dist[adjx][adjy] = dist[x][y] + 1


n, m = -1, -1
while n != 0 and m != 0:
    n, m = map(int, input().split())
    if n != 0 and m != 0:
        rows = int(input())
        maze = [['.' for _ in range(m)] for _ in range(n)]
        for _ in range(rows):
             arr = list(map(int, input().split()))
             for i in range(2, len(arr)):
                 maze[arr[0]][arr[i]] = '#'
        s_row, s_col = map(int, input().split())
        e_row, e_col = map(int, input().split())

        dist = [[ -1 for _ in range(m)] for _ in range(n)]
        BFS(m,n,maze,dist,s_row,s_col)
        print(dist[e_row][e_col])
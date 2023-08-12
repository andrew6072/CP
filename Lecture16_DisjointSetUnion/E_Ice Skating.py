dRow = [-1, 0, 1, 0]
dCol = [0, 1, 0, -1]

def IsValid(m, n, maze, visited, row, col):
    if row < 0 or col < 0 or row >= n or col >= m:
        return False
    if visited[row][col]:
        return False
    if maze[row][col] != '.':
        return False
    return True


def dfs(m, n, maze, visited, row, col):
    visited[row][col] = True
    for i in range(4):
        adj_row = row + dRow[i]
        adj_col = col + dCol[i]
        if IsValid(m, n, maze, visited, row, col):
            dfs(m, n, maze, visited, adj_row, adj_col)


def findNumComponent(m, n, maze):
    count = 0
    visited = [[False for _ in range(m)] for _ in range(n)]
    for i in range(n):
        for j in range(m):
            if IsValid(m, n, maze, visited, i, j):
                dfs(m, n, maze, visited, i, j)
                count += 1
    return count


N = int(input())
m = -1
n = -1
snow_points = []
for _ in range(N):
    j, i = map(int, input().split())
    snow_points.append((i, j))
    m = max(m, j)
    n = max(n, i)

maze = [['#' for _ in range(m)] for _ in range(n)]
for point in snow_points:
    maze[point[0]-1][point[1]-1] = '.'
ans = findNumComponent(m, n, maze)
print(ans)

dRow = [-1, 0, 1, 0]
dCol = [0, 1, 0, -1]


def IsValid(m, n, maze, visited, row, col):
    if row < 1 or col < 1 or row >= n-1 or col >= m-1:
        return False
    if visited[row][col]:
        return False
    if maze[row][col] != '.':
        return False
    return True


def dfs(count, component, m, n, maze, visited, row, col):
    visited[row][col] = True
    component.append((count, row, col))
    for k in range(4):
        adj_i = row + dRow[k]
        adj_j = col + dCol[k]
        if IsValid(m, n, maze, visited, adj_i, adj_j):
            dfs(count, component, m, n, maze, visited, adj_i, adj_j)


def NumComponents(m, n, maze):
    count = 0
    visited = [[ False for _ in range(m)] for _ in range(n)]
    component = []
    for i in range(1, n-1):
        for j in range(1, m-1):
            if IsValid(m,n,maze,visited,i,j):
                dfs(count, component, m, n, maze, visited, i, j)
                count += 1
    return count, component


n, m = map(int, input().split())
maze = []
for i in range(n):
    ele_maze = input()
    maze.append(ele_maze)
count, component = NumComponents(m,n,maze)
print(count)
print(component)
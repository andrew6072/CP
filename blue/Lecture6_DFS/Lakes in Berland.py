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


def IsOcean(m, n, maze, row, col): # only check cells that are not in border with ocean
    if maze[row][col] == '.' and (row == 0 or row == n - 1 or col == 0 or col == m - 1):
            return True
    return False


def dfs(count, component, m, n, maze, visited, row, col):
    visited[row][col] = True
    stack = []
    stack.append((row, col))
    num_cell_in_component = 0 # stores number of cells in the component that we are considering
    isOcean = False
    while len(stack) != 0:
        cell = stack.pop()
        num_cell_in_component += 1
        component.append((count, cell[0], cell[1])) # stores tuples of (so thu tu of component, row coprdinate of a cell in the component, col coordinate)
        for i in range(4):
            adj_i = cell[0] + dRow[i]
            adj_j = cell[1] + dCol[i]
            if IsValid(m,n, maze, visited, adj_i, adj_j):
                visited[adj_i][adj_j] = True
                stack.append((adj_i, adj_j))
            if IsOcean(m, n, maze, adj_i, adj_j):
                isOcean = True

    if isOcean:
        while num_cell_in_component > 0:
            component.pop()
            num_cell_in_component -= 1

    return num_cell_in_component


def NumComponents(m, n, maze):
    count = 0
    visited = [[ False for _ in range(m)] for _ in range(n)]
    component = [] # stores tuples of (so thu tu of component, row coordinate of a cell in the component, col coordinate)
    component_size = [] # list of tuples (so thu tu component, number of cell in that component)
    for i in range(1, n-1):
        for j in range(1, m-1):
            if IsValid(m,n,maze,visited,i,j):
                num_cell_in_component = dfs(count, component, m, n, maze, visited, i, j)
                if num_cell_in_component != 0:
                    component_size.append((count, num_cell_in_component)) # array of tuple (so thu tu component, number of cell in that component)
                    count += 1
    return count, component, component_size


# input
n, m, k = map(int, input().split())
maze = []
for i in range(n):
    ele_maze = list(input().strip())
    maze.append(ele_maze)
count_num_of_lakes_in_maze, components, component_size = NumComponents(m,n,maze)
component_size.sort(key=lambda s: s[1])
number_lake_filled = count_num_of_lakes_in_maze - k # number of lakes that we need to fill to have total k lakes in the map

number_water_filled = 0 #number of water cells in the component that is needed to fill with earth
for i in range(number_lake_filled):
    comp_size = component_size[i]
    number_water_filled += comp_size[1]
    for comp in components:
        if comp[0] == comp_size[0]:
            maze[comp[1]][comp[2]] = '*'

#output
print(number_water_filled)
for i in range(n):
    for j in range(m):
        print(maze[i][j],end='')
    print()
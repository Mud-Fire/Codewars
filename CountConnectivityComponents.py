import collections


def dogrid(grid, i, j):
    mydeque = collections.deque([(i, j)])
    size = 0
    while mydeque:
        i, j = mydeque.pop()
        if 0 <= i < len(grid) and 0 <= j  < len(grid[0]) and grid[i][j] == ' ':
            grid[i][j] = "#"
            mydeque.extend([(i+1, j),(i-1, j),(i, j+1),(i, j-1)])
            size += i % 2 ==1 and j % 3 == 1

    return size


def components(grid):
    grid_list = grid.split('\n')
    grid = []
    for i in grid_list:
        grid.append(list(j for j in i))
    print(grid)
    len_row = len(grid_list)
    len_col = len(grid_list[0])
    cells = ((i, j) for i in range(len_row) for j in range(len_col))
    result = collections.Counter(dogrid(grid,i, j) for (i, j) in cells if grid[i][j] == ' ')
    return sorted(result.items(),reverse=True)



print(components('''\
+--+--+--+
|  |     |
+  +  +--+
|  |  |  |
+--+--+--+'''))

print([(3, 1), (2, 1), (1, 1)])

def land(grid, n):
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == 1:
                n += 4
                if 0 < i and grid[i-1][j] == 1:
                    n -= 2
                if 0 < j and grid[i][j-1] == 1:
                    n -= 2
    print(n)


grid = [[0,1,0,0],
 [1,1,1,0],
 [0,1,0,0],
 [1,1,0,0]]
land(grid, 0)

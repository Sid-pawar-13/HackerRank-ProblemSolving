import numpy as np

def cavityMap(grid):
    indexes = []
    for i in range(1, len(grid)-1):
        for j in range(1, len(grid[i])-1):
            if grid[i][j-1] < grid[i][j] > grid[i][j+1]:
                if grid[i-1][j] < grid[i][j] > grid[i+1][j]:
                    indexes.append((i,j))
    for i,j in indexes:
        grid[i] = grid[i][:j] + "X" + grid[i][j+1:]
    return grid

print(cavityMap(['1112','1912','1892','1234']))

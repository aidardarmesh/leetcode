from typing import *

def spiral_matrix(R, C):
    grid = [[0]*C for _ in range(R)]
    seen = [[False]*C for _ in range(R)]
    r = c = di = 0
    dr = [0, 1, 0, -1]
    dc = [1, 0, -1, 0]
    counter = 1

    for _ in range(R*C):
        grid[r][c] = counter
        seen[r][c] = True
        counter += 1
        nr, nc = r + dr[di], c + dc[di]

        if 0 <= nr < R and 0 <= nc < C and not seen[nr][nc]:
            r, c = nr, nc
        else:
            di = (di+1) % 4
            r, c = r + dr[di], c + dc[di]

    return grid

print(spiral_matrix(3,3))


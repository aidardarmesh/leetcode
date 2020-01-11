from typing import *

class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        m = [[0]*n for _ in range(n)]
        seen = [[False]*n for _ in range(n)]
        counter = 1
        dirs = [(0,1),(1,0),(0,-1),(-1,0)]
        dir_idx = 0
        r, c = 0, 0
        
        for i in range(n):
            for j in range(n):
                m[r][c] = counter
                seen[r][c] = True
                counter += 1
                
                nr, nc = r + dirs[dir_idx][0], c + dirs[dir_idx][1]
                
                if 0 <= nr < n and 0 <= nc < n and not seen[nr][nc]:
                    r, c = nr, nc
                else:
                    dir_idx = (dir_idx+1) % 4
                    r, c = r + dirs[dir_idx][0], c + dirs[dir_idx][1]
        
        return m

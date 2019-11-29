from typing import *

class Solution:
    def closedIsland(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0
        
        N = len(grid)
        M = len(grid[0])
        islands = 0
        
        for i in range(1, N-1):
            for j in range(1, M-1):
                if grid[i][j] == 0:
                    grid[i][j] = 1
                    touched_border = False
                    
                    # BFS
                    queue = [(i,j)]
                    
                    while queue:
                        x,y = queue.pop(0)
                        
                        for ni, nj in [(x-1,y),(x+1,y),(x,y-1),(x,y+1)]:
                            if grid[ni][nj] == 0:
                                grid[ni][nj] = 1

                                if not (ni == 0 or ni == N-1 or nj == 0 or nj == M-1):
                                    queue.append((ni,nj))
                                else:
                                    touched_border = True
                    
                    if not touched_border:
                        islands += 1
        
        return islands

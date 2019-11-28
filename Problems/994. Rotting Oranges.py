from typing import *

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        N = len(grid)
        M = len(grid[0])
        fresh = 0
        queue = []
        
        # main trick - get all rottened oranges
        for i in range(N):
            for j in range(M):
                if grid[i][j] == 2:
                    queue.append((i, j))
                elif grid[i][j]:
                    fresh += 1
        
        # consider edge cases
        if not queue:
            if fresh:
                return -1
            
            return 0
        
        time = -1
        
        while queue:
            size = len(queue)
            
            for _ in range(size):
                i, j = queue.pop(0)
                
                for x, y in [(i+1, j), (i, j+1), (i-1, j), (i, j-1)]:
                    if 0 <= x < N and 0 <= y < M and grid[x][y] == 1:
                        grid[x][y] = 2
                        fresh -= 1
                        queue.append((x, y))
            
            time += 1
        
        return time if fresh == 0 else -1

from typing import *

class Solution:
    def numDistinctIslands(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0
        
        n = len(grid)
        m = len(grid[0])
        
        from collections import deque
        
        uniques = set()
        
        def bfs(i,j):
            deq = deque()
            deq.append((i,j))
            start_i = i
            start_j = j
            offsets = []
            
            while deq:
                i, j = deq.popleft()
                offsets.append((start_i-i, start_j-j))
                
                for ni, nj in [(i-1,j),(i+1,j),(i,j-1),(i,j+1)]:
                    if 0 <= ni < n and 0 <= nj < m and grid[ni][nj]:
                        grid[ni][nj] = 0
                        deq.append((ni,nj))
            
            uniques.add(tuple(sorted(offsets)))
        
        for i in range(n):
            for j in range(m):
                if grid[i][j]:
                    bfs(i,j)
        
        return len(uniques)

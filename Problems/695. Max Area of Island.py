from typing import *

class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        N = len(grid)
        M = len(grid[0])
        max_ = 0
        
        def dfs(x, y):
            if not grid[x][y]:
                return 0
            
            area = 1
            grid[x][y] = 0
            
            for ni, nj in [(x-1,y), (x+1,y), (x,y-1), (x,y+1)]:
                if 0 <= ni < N and 0 <= nj < M and grid[ni][nj]:
                    area += dfs(ni, nj)
            
            return area
        
        for i in range(N):
            for j in range(M):
                max_ = max(max_, dfs(i,j))
        
        return max_

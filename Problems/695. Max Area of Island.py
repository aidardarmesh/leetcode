from typing import *

class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        N = len(grid)
        M = len(grid[0])
        max_ = 0
        
        def dfs(x,y):
            if 0 <= x < N and 0 <= y < M and grid[x][y]:
                grid[x][y] = 0
                return 1 + dfs(x-1,y) + dfs(x+1,y) + dfs(x,y-1) + dfs(x,y+1)
            
            return 0
        
        for i in range(N):
            for j in range(M):
                max_ = max(max_, dfs(i,j))
        
        return max_

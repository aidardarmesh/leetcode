from typing import *

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        '''
        Strategy is to "draw" lands in water
        '''
        if not grid:
            return 0
        
        N = len(grid)
        M = len(grid[0])
        islands = 0
        
        for i in range(N):
            for j in range(M):
                if grid[i][j] == '1':
                    grid[i][j] = '0'
                    islands += 1
                    queue = [(i,j)]
                    
                    while queue:
                        x,y = queue.pop()
                        
                        for ni, nj in [(x+1,y),(x-1,y),(x,y+1),(x,y-1)]:
                            if 0 <= ni < N and 0 <= nj < M:
                                if grid[ni][nj] == '1':
                                    grid[ni][nj] = '0'
                                    queue.append((ni,nj))
        
        return islands

s = Solution()

islands = s.numIslands([["1","1","0","0","0"],["1","1","0","0","0"],["0","0","1","0","0"],["0","0","0","1","1"]])

print(islands)
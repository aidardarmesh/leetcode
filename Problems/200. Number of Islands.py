from typing import *

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        
        N = len(grid)
        M = len(grid[0])
        
        islands = self.lands = 0
        visited = {}
        
        for i in range(N):
            for j in range(M):
                if grid[i][j] == '1':
                    visited[(i,j)] = False
                    self.lands += 1
        
        def get_unvisited():
            for key, val in visited.items():
                if not val:
                    return key
            
            return None
        
        def bfs(s):
            queue = [s]
            visited[s] = True
            self.lands -= 1
            
            while queue:
                i,j = queue.pop(0)
                
                for x,y in [(i+1,j),(i-1,j),(i,j+1),(i,j-1)]:
                    if 0 <= x < N and 0 <= y < M:
                        if grid[x][y] == '1' and not visited[(x,y)]:
                            visited[(x,y)] = True
                            self.lands -= 1
                            queue.append((x,y))
        
        while self.lands:
            bfs(get_unvisited())
            islands += 1
        
        return islands

s = Solution()

islands = s.numIslands([["1","1","0","0","0"],["1","1","0","0","0"],["0","0","1","0","0"],["0","0","0","1","1"]])

print(islands)
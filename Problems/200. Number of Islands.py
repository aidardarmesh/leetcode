from typing import *

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        
        N = len(grid)
        M = len(grid[0])
        
        uf = {}
        self.islands = 0
        
        for i in range(N):
            for j in range(M):
                if grid[i][j] == "1":
                    uf[i*M+j] = i*M+j
                    self.islands += 1
        
        def get_item(i, j):
            if i < 0 or i >= N or j < 0 or j >= M:
                return "0"
            
            return grid[i][j]
        
        def find_set(v):
            if v == uf[v]:
                return v
            
            uf[v] = find_set(uf[v])
            return uf[v]
        
        def union_sets(u, v):
            u_root = find_set(u)
            v_root = find_set(v)
            
            if u_root != v_root:
                uf[u_root] = v_root
                self.islands -= 1
                
        for i in range(N):
            for j in range(M):
                if get_item(i, j) == "1":
                    if get_item(i, j-1) == "1":
                        union_sets(i*M+j, i*M+j-1)
                    
                    if get_item(i-1, j) == "1":
                        union_sets(i*M+j, (i-1)*M+j)
                    
                    if get_item(i, j+1) == "1":
                        union_sets(i*M+j, i*M+j+1)
                    
                    if get_item(i+1, j) == "1":
                        union_sets(i*M+j, (i+1)*M+j)
        
        return self.islands

s = Solution()

islands = s.numIslands([["1","1","0","0","0"],["1","1","0","0","0"],["0","0","1","0","0"],["0","0","0","1","1"]])

print(islands)
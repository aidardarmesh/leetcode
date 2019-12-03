from typing import *

class UF:
    def __init__(self, n):
        self.p = {i:i for i in range(n)}
    
    def find(self, x):
        if x == self.p[x]:
            return x
        
        self.p[x] = self.find(self.p[x])
        
        return self.p[x]
    
    def union(self, x, y):
        self.p[self.find(x)] = self.find(y)


class Solution:
    def regionsBySlashes(self, grid: List[str]) -> int:
        N = len(grid)
        uf = UF(4*N*N)
        
        for r, row in enumerate(grid):
            for c, val in enumerate(row):
                root = 4*(r*N + c)
                
                if val == ' ':
                    uf.union(root + 0, root + 1)
                    uf.union(root + 1, root + 2)
                    uf.union(root + 2, root + 3)
                    uf.union(root + 3, root + 0)
                elif val == '/':
                    uf.union(root + 0, root + 1)
                    uf.union(root + 2, root + 3)
                elif val == '\\':
                    uf.union(root + 0, root + 2)
                    uf.union(root + 1, root + 3)
                
                # north
                if r-1 >= 0:
                    uf.union(root + 0, root + 3 - 4*N)
                
                # south
                if r+1 < N:
                    uf.union(root + 3, root + 0 + 4*N)
                    
                # west
                if c-1 >= 0:
                    uf.union(root + 1, root + 2 - 4*1)
                
                # east
                if c+1 < N:
                    uf.union(root + 2, root + 1 + 4*1)
        
        return sum([x == uf.find(x) for x in range(4*N*N)])

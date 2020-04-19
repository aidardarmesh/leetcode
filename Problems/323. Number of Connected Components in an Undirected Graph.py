from typing import *

class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        uf = {i:i for i in range(n)}
        self.cnt = n
        
        def find_set(v):
            if v == uf[v]:
                return v
            
            uf[v] = find_set(uf[v])
            
            return uf[v]
        
        def union_sets(u,v):
            u = find_set(u)
            v = find_set(v)
            
            if u != v:
                uf[v] = u
                self.cnt -= 1
        
        for u, v in edges:
            union_sets(u,v)
        
        return self.cnt

from typing import *

class Solution:
    def findCircleNum(self, M: List[List[int]]) -> int:
        N = len(M)
        self.circles = N
        uf = {x:x for x in range(N)}
        
        def find_set(v):
            if v == uf[v]:
                return v
            
            uf[v] = find_set(uf[v])
            return uf[v]
        
        def union_sets(u,v):
            u = find_set(u)
            v = find_set(v)
            
            if u != v:
                uf[u] = v
                self.circles -= 1
                
        for i in range(N):
            for j in range(N):
                if M[i][j]:
                    union_sets(i, j)
        
        return self.circles

from typing import *


class Solution:
    def gardenNoAdj(self, N: int, paths: List[List[int]]) -> List[int]:
        fs = [1,2,3,4]
        gs = {}
        res = [0 for _ in range(N+1)]
        
        for i in range(1, N+1):
            gs[i] = []
        
        for g1, g2 in paths:
            if g1 in gs:
                if not g2 in gs[g1]:
                    gs[g1].append(g2)
            
            if g2 in gs:
                if not g1 in gs[g2]:
                    gs[g2].append(g1)
        
        for i in gs:
            for f in fs:
                free = True
                
                for neigh in gs[i]:
                    if res[neigh] == f:
                        free = False
                        break
                
                if free:
                    res[i] = f
                    break
        
        res.pop(0)
        
        return res

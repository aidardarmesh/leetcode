from typing import *

class Solution:
    def numIslands2(self, m: int, n: int, positions: List[List[int]]) -> List[int]:
        m, n = n, m
        uf = {(i,j):(i,j) for i in range(n) for j in range(m)}
        lands = set()
        res = []
        cnt = 0
        
        def find_set(v):
            if v == uf[v]:
                return v
            
            uf[v] = find_set(uf[v])
            
            return uf[v]
        
        for i, j in positions:
            cnt += 1
            
            if not (i,j) in lands:
                lands.add((i,j))
            else:
                cnt -= 1
            
            for ni, nj in [(i-1,j),(i+1,j),(i,j-1),(i,j+1)]:
                if 0 <= ni < n and 0 <= nj < m and (ni,nj) in lands:
                    u = find_set((ni,nj))
                    v = find_set((i,j))
                    
                    if u != v:
                        uf[v] = u
                        cnt -= 1
            
            res.append(cnt)
        
        return res

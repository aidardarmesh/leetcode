from typing import *

class Solution:
    def candyCrush(self, m: List[List[int]]) -> List[List[int]]:
        N = len(m)
        M = len(m[0])
        
        while True:
            crush = set()
            
            # scan
            for i in range(N):
                for j in range(M):
                    if i > 1 and m[i][j] and m[i][j] == m[i-1][j] == m[i-2][j]:
                        crush |= {(i,j),(i-1,j),(i-2,j)}
                    
                    if j > 1 and m[i][j] and m[i][j] == m[i][j-1] == m[i][j-2]:
                        crush |= {(i,j),(i,j-1),(i,j-2)}
            
            if not crush:
                break
            
            # crush
            for i, j in crush:
                m[i][j] = 0
            
            # down
            for j in range(M):
                idx = N-1
                
                for i in range(N-1, -1, -1):
                    if m[i][j]:
                        m[idx][j] = m[i][j]
                        idx -= 1
                
                for i in range(idx, -1, -1):
                    m[i][j] = 0
        
        return m

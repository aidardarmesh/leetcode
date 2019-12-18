from typing import *

class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        if not matrix:
            return []
        
        R = len(matrix)
        C = len(matrix[0])
        seen = [[False]*C for _ in range(R)]
        dr = [0, 1, 0, -1]
        dc = [1, 0, -1, 0]
        r = c = di = 0
        ans = []
        
        for _ in range(R*C):
            ans.append(matrix[r][c])
            seen[r][c] = True
            
            nr, nc = r + dr[di], c + dc[di]
            
            if 0 <= nr < R and 0 <= nc < C and not seen[nr][nc]:
                r, c = nr, nc
            else:
                di = (di + 1) % 4
                r, c = r + dr[di], c + dc[di]
        
        return ans

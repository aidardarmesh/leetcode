from typing import *

class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        n = len(board)
        m = len(board[0])
        neighs = [
            (-1,-1),(-1,0),(-1,1),(0,-1),
            (0,1),(1,-1),(1,0),(1,1)
        ]
        WAS_ALIVE = NOW_DEAD = -1
        WAS_DEAD = NOW_ALIVE = 2
        
        for r in range(n):
            for c in range(m):
                live = 0
                
                for dr, dc in neighs:
                    nr = r + dr
                    nc = c + dc
                    
                    if 0 <= nr < n and 0 <= nc < m and (board[nr][nc] == 1 or board[nr][nc] == WAS_ALIVE):
                        live += 1
                
                if board[r][c] == 1 and (live < 2 or live > 3):
                    board[r][c] = NOW_DEAD
                
                if board[r][c] == 0 and live == 3:
                    board[r][c] = NOW_ALIVE
        
        # rerender
        for r in range(n):
            for c in range(m):
                if board[r][c] == NOW_ALIVE:
                    board[r][c] = 1
                elif board[r][c] == NOW_DEAD:
                    board[r][c] = 0

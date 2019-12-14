from typing import *

class Solution:
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        if not rooms:
            return
        
        EMPTY = 2147483647
        GATE = 0
        WALL = -1
        N = len(rooms)
        M = len(rooms[0])
        queue = []
        
        for i in range(N):
            for j in range(M):
                if rooms[i][j] == GATE:
                    queue.append((i,j))
        
        while queue:
            i, j = queue.pop(0)
            
            for ni, nj in [(i-1,j),(i+1,j),(i,j-1),(i,j+1)]:
                if ni < 0 or ni >= N or nj < 0 or nj >= M:
                    continue
                
                if rooms[ni][nj] == EMPTY:
                    rooms[ni][nj] = rooms[i][j] + 1
                    queue.append((ni,nj))

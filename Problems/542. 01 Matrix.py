from typing import *

class Solution:
    def updateMatrix(self, matrix: List[List[int]]) -> List[List[int]]:
        N = len(matrix)
        M = len(matrix[0])
        dist = [[float('inf') for j in range(M)] for i in range(N)]
        queue = []
        
        for i in range(N):
            for j in range(M):
                if matrix[i][j] == 0:
                    dist[i][j] = 0
                    queue.append((i,j))
        
        while queue:
            i, j = queue.pop(0)
            
            for ni, nj in [(i-1,j),(i+1,j),(i,j-1),(i,j+1)]:
                if 0 <= ni < N and 0 <= nj < M:
                    if dist[i][j] + 1 < dist[ni][nj]:
                        dist[ni][nj] = dist[i][j] + 1
                        queue.append((ni,nj))
        
        return dist

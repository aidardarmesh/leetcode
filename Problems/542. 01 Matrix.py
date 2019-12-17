from typing import *

class Solution:
    def updateMatrix(self, matrix: List[List[int]]) -> List[List[int]]:
        queue = []
        visited = set()
        N = len(matrix)
        M = len(matrix[0])
        
        for i in range(N):
            for j in range(M):
                if matrix[i][j] == 0:
                    queue.append((i,j))
        
        while queue:
            i, j = queue.pop(0)
            
            if (i,j) in visited:
                continue
                
            visited.add((i,j))
            min_ = float('inf')
            
            for ni,nj in [(i-1,j),(i+1,j),(i,j-1),(i,j+1)]:
                if 0 <= ni < N and 0 <= nj < M:
                    if not (ni,nj) in visited:
                        queue.append((ni,nj))
                    else:
                        min_ = min(min_, matrix[ni][nj])
            
            if matrix[i][j] != 0:
                matrix[i][j] = min_ + 1
        
        return matrix

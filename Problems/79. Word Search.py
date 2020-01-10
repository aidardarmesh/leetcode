from typing import *

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        if not board or not word:
            return False
        
        N = len(board)
        M = len(board[0])
        visited = set()
        
        def backtrack(i, j, k, visited):
            if word[k] != board[i][j]:
                return False
            
            if k == len(word)-1:
                return True
            
            for ni, nj in [(i-1,j),(i+1,j),(i,j-1),(i,j+1)]:
                if 0 <= ni < N and 0 <= nj < M and not (ni,nj) in visited:
                    visited.add((ni,nj))
                    
                    if backtrack(ni,nj,k+1,visited):
                        return True
                    
                    visited.discard((ni,nj))
        
        for i in range(N):
            for j in range(M):
                visited.add((i,j))
                
                if backtrack(i, j, 0, visited):
                    return True
                
                visited.discard((i,j))
        
        return False

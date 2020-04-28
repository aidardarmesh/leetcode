from typing import *

class Solution:
    def minFallingPathSum(self, A: List[List[int]]) -> int:
        n, m = len(A), len(A[0])
        dp = [[None]*m for _ in range(n)]
        
        def helper(r, c):
            if not (0 <= r < n and 0 <= c < m):
                return float('inf')
            
            if dp[r][c] is not None:
                return dp[r][c]
            
            if r == n-1:
                dp[r][c] = A[r][c]
                
                return dp[r][c]
            
            cand = float('inf')
            
            for dc in range(-1, 2):
                cand = min(cand, helper(r+1, c+dc))
            
            dp[r][c] = cand + A[r][c]
            
            return dp[r][c]
            
        return min([helper(0, c) for c in range(m)])

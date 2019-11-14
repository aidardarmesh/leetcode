from typing import *


class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        memo = [[-1 for _ in range(n)] for _ in range(m)]
        
        def paths(i, j, memo):
            if i < 0 or j < 0:
                return 0
            elif memo[i][j] != -1:
                return memo[i][j]
            elif i == 0 and j == 0:
                memo[i][j] = 1
            else:
                memo[i][j] = paths(i-1, j, memo) + paths(i, j-1, memo)
            
            return memo[i][j]
        
        return paths(m-1, n-1, memo)

s = Solution()

assert s.uniquePaths(3, 2) == 3
assert s.uniquePaths(7, 3) == 28

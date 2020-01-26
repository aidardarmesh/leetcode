from typing import *

class Solution:
    def maxSideLength(self, mat: List[List[int]], threshold: int) -> int:
        if not mat:
            return 0
        
        max_square = 0
        dp = [[0] * (len(mat[0]) + 1) for _ in range(len(mat) + 1)]
        
        for i in range(1, len(mat) + 1):
            for j in range(1, len(mat[0]) + 1):
                dp[i][j] = dp[i - 1][j] + dp[i][j - 1] - dp[i - 1][j - 1] + mat[i - 1][j - 1]
                l = 1
                r = min(i, j)
                
                while l <= r:
                    k = (l + r) // 2
                    cur_sum = dp[i][j] - dp[i - k][j] - dp[i][j - k] + dp[i - k][j - k]
                    if cur_sum <= threshold:
                        max_square = max(max_square, k)
                        l = k + 1
                    else:
                        r = k - 1
        
        return max_square
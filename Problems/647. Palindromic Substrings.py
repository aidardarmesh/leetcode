from typing import *

class Solution:
    def countSubstrings(self, s: str) -> int:
        if not s:
            return 0
        
        n = len(s)
        cnt = n
        dp = [[1 for j in range(n)] for i in range(n)]
        
        for d in range(1, n):
            for i in range(n-d):
                j = i + d
                
                if s[i] == s[j] and dp[i+1][j-1]:
                    cnt += 1
                else:
                    dp[i][j] = 0
        
        return cnt

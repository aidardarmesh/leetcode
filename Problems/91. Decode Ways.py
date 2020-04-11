from typing import *

class Solution:
    def numDecodings(self, s: str) -> int:
        n = len(s)
        dp = [0 for _ in range(n+1)]
        dp[n] = 1
        
        for i in range(n-1, -1, -1):
            if s[i] == '0':
                continue
            elif s[i] == '1':
                dp[i] = dp[i+1]
                
                if i+2 <= n:
                    dp[i] += dp[i+2]
            elif s[i] == '2':
                dp[i] = dp[i+1]
                
                if i+2 <= n and s[i+1] <= '6':
                    dp[i] += dp[i+2]
            else:
                dp[i] = dp[i+1]
        
        return dp[0]

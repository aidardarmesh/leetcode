from typing import *

class Solution:
    def numDecodings(self, s: str) -> int:
        if not s:
            return 0
        
        n = len(s)
        dp = [0 for _ in range(n+1)]
        dp[n] = 1
        
        for i in range(n-1, -1, -1):
            if s[i] == '0':
                continue
                
            dp[i] = dp[i+1]
            
            if i+1 < n:
                if s[i] == '1' or (s[i] == '2' and s[i+1] <= '6'):
                    dp[i] += dp[i+2]
        
        return dp[0]

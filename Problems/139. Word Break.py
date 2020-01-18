from typing import *

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        n = len(s)
        words = set(wordDict)
        dp = [False]*(n+1)
        dp[0] = True
        
        for j in range(1, n+1):
            for i in range(j):
                if dp[i] and s[i:j] in words:
                    dp[j] = True
        
        return dp[n]

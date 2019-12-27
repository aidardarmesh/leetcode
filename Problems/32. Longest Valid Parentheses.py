from typing import *

class Solution:
    def longestValidParentheses(self, s: str) -> int:
        n = len(s)
        dp = [0 for _ in range(n)]
        max_ = 0

        for i in range(1, n):
            if s[i] == ')':
                if s[i-1] == '(':
                    dp[i] = 2 + (dp[i-2] if i-2 >= 0 else 0)
                else:
                    nei = i-dp[i-1]-1

                    dp[i] = dp[i-1] + 2 + (dp[nei-1] if nei-1 >= 0 else 0)

                max_ = max(max_, dp[i])
        
        return max_

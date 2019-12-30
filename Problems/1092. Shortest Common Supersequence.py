from typing import *

class Solution:
    def shortestCommonSupersequence(self, str1: str, str2: str) -> str:
        n = len(str1)
        m = len(str2)
        dp = [[0 for j in range(m+1)] for i in range(n+1)]
        
        # map for longest common subsequence
        for i in range(1, n+1):
            for j in range(1, m+1):
                if str1[i-1] == str2[j-1]:
                    dp[i][j] = dp[i-1][j-1] + 1
                else:
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1])
        
        # backtrack to get shortest common subsequence
        ans = []
        
        while i or j:
            if i > 0 and dp[i][j] == dp[i-1][j]:
                ans.append(str1[i-1])
                i -= 1
            elif j > 0 and dp[i][j] == dp[i][j-1]:
                ans.append(str2[j-1])
                j -= 1
            else:
                ans.append(str1[i-1])
                i -= 1
                j -= 1
        
        return ''.join(ans[::-1])

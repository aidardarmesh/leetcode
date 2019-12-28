from typing import *

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        n = len(s)
        words = set(wordDict)
        dp = [False for _ in range(n+1)]
        dp[0] = True
        
        for i in range(1, n+1):
            for j in range(i):
                if dp[j] and s[j:i] in words:
                    dp[i] = True
        
        return dp[n]

s = Solution()

print(s.wordBreak("applepenapple", ["apple", "pen"]))
print(s.wordBreak("catsandog", ["cats", "cat", "dog", "sand", "and"]))
print(s.wordBreak("leetcode", ["leet", "code"]))

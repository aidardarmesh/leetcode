from typing import *

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [float('inf')]*(amount+1)
        dp[0] = 0
        
        for target in range(1, amount+1):
            for coin in coins:
                if target >= coin:
                    dp[target] = min(dp[target], dp[target-coin]+1)
        
        return dp[amount] if dp[amount] != float('inf') else -1

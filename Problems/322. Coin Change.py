from typing import *

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [float('inf')]*(amount+1)
        dp[0] = 0
        
        def change(target, coin):
            if target >= coin:
                return dp[target-coin]
            
            return float('inf')
        
        for target in range(1, amount+1):
            dp[target] = min([change(target, coin) for coin in coins]) + 1
        
        return dp[amount] if dp[amount] != float('inf') else -1

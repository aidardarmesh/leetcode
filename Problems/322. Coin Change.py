from typing import *

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = {i:float('inf') for i in range(amount+1)}
        dp[amount] = 0
        
        def changes(val):
            if val < 0 or val > amount:
                return float('inf')
            
            return dp[val]
        
        for i in range(amount-1, -1, -1):
            dp[i] = min([changes(i+coin) for coin in coins]) + 1
        
        return dp[0] if dp[0] != float('inf') else -1

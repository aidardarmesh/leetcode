from typing import *

class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        f1, f2 = cost[0], cost[1]
        
        for i in range(2, len(cost)):
            f1, f2 = f2, min(f1, f2) + cost[i]
        
        return min(f1, f2)

from typing import *

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0
        
        res = 0
        min_price = prices.pop(0)
        
        for price in prices:
            if min_price >= price:
                min_price = price
            else:
                res = max(res, price-min_price)
        
        return res

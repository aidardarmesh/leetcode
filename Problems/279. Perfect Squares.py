from typing import *

class Solution:
    def numSquares(self, n: int) -> int:
        def sqrt(n):
            left, right = 0, n
            cand = 0
            
            while left <= right:
                mid = (left+right)//2
                mid_sqr = mid ** 2
                
                if mid_sqr == n:
                    return mid
                elif mid_sqr < n:
                    cand = max(cand, mid)
                    left = mid + 1
                else:
                    right = mid - 1
            
            return cand
        
        root = sqrt(n)
        squares = [i**2 for i in range(1, root+1)]
        queue = {n}
        level = 0
        
        while queue:
            level += 1
            next_queue = set()
            
            for remainder in queue:
                for square in squares:
                    if remainder == square:
                        return level
                    elif remainder < square:
                        break
                    else:
                        next_queue.add(remainder-square)
            
            queue = next_queue
        
        return level

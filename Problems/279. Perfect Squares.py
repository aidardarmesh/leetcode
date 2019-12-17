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
        squares = set([i**2 for i in range(root)])
        
        def is_divided_by(n, count):
            if count == 1:
                return n in squares
            
            for k in squares:
                if is_divided_by(n-k, count-1):
                    return True
            
            return False
        
        for count in range(1, n+1):
            if is_divided_by(n, count):
                return count

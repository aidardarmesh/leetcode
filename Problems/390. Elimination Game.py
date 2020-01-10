from typing import *

class Solution:
    def lastRemaining(self, n: int) -> int:
        head = 1
        step = 1
        left = True
        
        while n > 1:
            if left or n % 2 == 1:
                head += step
            
            step *= 2
            n //= 2
            left = not left
        
        return head

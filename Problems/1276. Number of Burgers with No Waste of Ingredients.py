from typing import *

class Solution:
    def numOfBurgers(self, tomatoSlices: int, cheeseSlices: int) -> List[int]:
        N = tomatoSlices
        M = cheeseSlices
        
        l, r = 0, M
        
        while l <= r:
            m = (l+r) // 2
            T = 4*m + 2*(M-m)
            
            if T == N:
                return [m, M-m]
            elif T > N:
                r = m-1
            else:
                l = m+1
        
        return []

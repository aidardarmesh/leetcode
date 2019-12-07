from typing import *

class Solution:
    def kthGrammar(self, N: int, K: int) -> int:
        def helper(N, K):
            if N == 1 or N == 0:
                return [0, 1]
            
            values = helper(N-1, (K+1)//2)

            if values[(K-1)%2] == 0:
                return [0, 1]

            return [1, 0]
        
        values = helper(N-1, (K+1)//2)
        
        return values[(K-1)%2]
        

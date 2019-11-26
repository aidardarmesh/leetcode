from typing import *

class Solution:
    def anagramMappings(self, A: List[int], B: List[int]) -> List[int]:
        D, P = {}, []
        
        for i, val in enumerate(B):
            D[val] = i
        
        for val in A:
            P.append(D[val])
        
        return P

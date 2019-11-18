from typing import *


class Solution:
    def findJudge(self, N: int, trust: List[List[int]]) -> int:
        trusted = [0 for _ in range(N+1)]
        
        for i, j in trust:
            trusted[i] -= 1
            trusted[j] += 1
        
        try:
            return trusted[1:].index(N-1) + 1
        except:
            return -1


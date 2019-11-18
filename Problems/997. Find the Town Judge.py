from typing import *


class Solution:
    def findJudge(self, N: int, trust: List[List[int]]) -> int:
        citizens = set([i for i in range(1, N+1)])
        naives = set()
        
        for pair in trust:
            naives.add(pair[0])
        
        candidates = (citizens - naives)
        
        if not candidates:
            return -1
        
        judge = candidates.pop()
        trusts_judge = set()
        
        for pair in trust:
            if pair[1] == judge:
                trusts_judge.add(pair[0])
        
        if len(citizens)-1 == len(trusts_judge):
            return judge
        
        return -1


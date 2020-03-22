from typing import *

class Solution:
    def numEquivDominoPairs(self, dominoes: List[List[int]]) -> int:
        pairs_cnt = {}
        res = 0
        
        for a, b in dominoes:
            if (a,b) in pairs_cnt:
                res += pairs_cnt[(a,b)]
                pairs_cnt[(a,b)] += 1
                continue
            
            if (b,a) in pairs_cnt:
                res += pairs_cnt[(b,a)]
                pairs_cnt[(b,a)] += 1
                continue
            
            pairs_cnt[(a,b)] = 1
        
        return res

from typing import *

class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        n, L = len(s), 10
        
        if n < L:
            return []
        
        a = 4
        aL = a ** L
        seen, ans = set(), set()
        to_int = {'A':0,'C':1,'G':2,'T':3}
        nums = [to_int.get(c) for c in s]
        h = 0
        
        for i in range(n-L+1):
            if i == 0:
                for j in range(L):
                    h = h*a + nums[j]
            else:
                h = h*a - nums[i-1] * aL + nums[i-1+L]
            
            if h in seen:
                ans.add(s[i:i+L])
            
            seen.add(h)
        
        return ans

from typing import *

class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        L = 10
        
        if len(s) < L:
            return []
        
        seq, ans = {}, []
        
        for i in range(len(s)-L+1):
            sub_str = s[i:i+L]
            seq[sub_str] = seq.get(sub_str, 0) + 1
        
        for sub_str in seq:
            if seq[sub_str] > 1:
                ans.append(sub_str)
        
        return ans

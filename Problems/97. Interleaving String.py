from typing import *

class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        def interleave(s1, i, s2, j, res, s3, k):
            if res == s3 and i == len(s1) and j == len(s2):
                return True
            
            if len(res) > 0 and k < len(s3) and res[-1] != s3[k]:
                return False
            
            ans = False
            
            if i < len(s1):
                ans |= interleave(s1, i+1, s2, j, res+s1[i], s3, k+1)
            
            if j < len(s2):
                ans |= interleave(s1, i, s2, j+1, res+s2[j], s3, k+1)
            
            return ans
        
        return interleave(s1, 0, s2, 0, '', s3, -1)

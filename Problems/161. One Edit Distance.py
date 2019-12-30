from typing import *

class Solution:
    def isOneEditDistance(self, s: str, t: str) -> bool:
        if s == t:
            return False
        
        ns = len(s)
        nt = len(t)
        
        if abs(ns-nt) > 1:
            return False
        
        i = j = 0
        actions = 1
        
        while i < ns and j < nt:
            if s[i] != t[j]:
                if actions:
                    actions -= 1
                else:
                    return False
                
                if ns < nt:
                    # insert
                    i -= 1
                elif ns > nt:
                    # delete
                    j -= 1
            
            i += 1
            j += 1
        
        return True

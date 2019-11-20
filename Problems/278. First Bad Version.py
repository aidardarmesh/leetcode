from typing import *


# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):

class Solution:
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        l, r = 1, n
        bad = 0
        
        while l <= r:
            m = (l+r) // 2
            
            if isBadVersion(m):
                bad = m
                r = m-1
            else:
                l = m+1
        
        return bad
        

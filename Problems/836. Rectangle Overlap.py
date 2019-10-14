from typing import *

class Solution:
    def isRectangleOverlap(self, rec1: List[int], rec2: List[int]) -> bool:
        def intersect(p_left, p_right, q_left, q_right):
            return max(p_left, q_left) < min(p_right, q_right)
        
        return  intersect(rec1[0], rec1[2], rec2[0], rec2[2]) \ 
            and intersect(rec1[1], rec1[3], rec2[1], rec2[3])

s = Solution()

assert s.isRectangleOverlap([0,0,2,2],[1,1,3,3]) == True
assert s.isRectangleOverlap([0,0,1,1],[1,0,2,1]) == False
assert s.isRectangleOverlap([0,0,2,2],[0,0,2,2]) == True
assert s.isRectangleOverlap([7,8,13,15],[10,8,12,20]) == True
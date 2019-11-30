from typing import *

class Solution:
    def removeInterval(self, intervals: List[List[int]], toBeRemoved: List[int]) -> List[List[int]]:
        '''
        1. interval does not intersect with int_remove
        2. interval totally inclused int_remove
        3. interval is touched from left part
        4. interval is touched from right part
        '''
        start = toBeRemoved[0]
        end = toBeRemoved[1]
        res = []
        
        for int_ in intervals:
            if start > int_[1] or end < int_[0]:
                res.append([int_[0], int_[1]])
            elif start > int_[0] and end < int_[1]:
                res.append([int_[0], start])
                res.append([end, int_[1]])
            elif start > int_[0]:
                res.append([int_[0], start])
            elif end < int_[1]:
                res.append([end, int_[1]])
        
        return res

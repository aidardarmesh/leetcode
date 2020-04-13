from typing import *

class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        from collections import deque
        
        row = deque([1])
        
        for i in range(rowIndex):
            size = len(row)
            
            for j in range(size-1):
                row[j] += row[j+1]
            
            row.appendleft(1)
        
        return row

s = Solution()

assert s.getRow(3) == [1,3,3,1]
assert s.getRow(1) == [1]
assert s.getRow(2) == [1,2,1]
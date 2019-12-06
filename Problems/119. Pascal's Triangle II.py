from typing import *

class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        row = [1]
        temp = 0
        
        for _ in range(rowIndex):
            size = len(row)
            
            for j in range(size):
                popped = row.pop(0)
                row.append(temp + popped)
                temp = popped
            
            temp = 0
            row.append(1)
            
        return row

s = Solution()

assert s.getRow(3) == [1,3,3,1]
assert s.getRow(1) == [1]
assert s.getRow(2) == [1,2,1]
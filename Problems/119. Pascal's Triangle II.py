from typing import *

class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        row = [1]
        
        while rowIndex:
            first_row = row[:] + [0]
            second_row = [0] + row[:]
            row = []
            
            for _ in range(len(first_row)):
                row.append(first_row.pop(0) + second_row.pop(0))
            
            rowIndex -= 1
        
        return row

s = Solution()

assert s.getRow(3) == [1,3,3,1]
assert s.getRow(1) == [1]
assert s.getRow(2) == [1,2,1]
from typing import *

class Solution:
    def get_item(self, arr: List[int], index):
        if index < 0 or index > len(arr)-1:
            return 0
        
        return arr[index]

    def generate(self, numRows: int) -> List[List[int]]:
        row = [1]
        res = []

        while numRows:
            res.append(row)
            new_row = []

            for i in range(len(row)+1):
                new_row.append(self.get_item(row, i-1) + self.get_item(row, i))
            
            row = new_row
            numRows -= 1
        
        return res

s = Solution()

assert s.generate(1) == [
    [1]
]

assert s.generate(2) == [
     [1],
    [1,1]
]

assert s.generate(3) == [
     [1],
    [1,1],
   [1,2,1],
]

assert s.generate(5) == [
     [1],
    [1,1],
   [1,2,1],
  [1,3,3,1],
 [1,4,6,4,1]
]
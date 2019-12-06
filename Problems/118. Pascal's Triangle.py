from typing import *

class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        triangle = []

        for row_num in range(numRows):
            row = [0 for _ in range(row_num+1)]
            row[0] = row[-1] = 1

            for j in range(1, len(row)-1):
                row[j] = triangle[row_num-1][j-1] + triangle[row_num-1][j]
            
            triangle.append(row)
        
        return triangle

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
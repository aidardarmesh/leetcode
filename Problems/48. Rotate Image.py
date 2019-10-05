from typing import *

class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)

        for i in range(n):
            for j in range(i, n):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
        
        for i in range(n):
            matrix[i].reverse()

s = Solution()
a = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]
b = [
    [1,2,3,4],
    [5,6,7,8],
    [9,10,11,12],
    [13,14,15,16]
]
c = [
    [1,2],
    [3,4]
]
d = [
    [1]
]
s.rotate(a)
s.rotate(b)
s.rotate(c)
s.rotate(d)
print(a)
print(b)
print(c)
print(d)
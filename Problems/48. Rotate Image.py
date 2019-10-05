from typing import *

class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)

        for i in range(0, n//2):
            for j in range(i, n-1-i):
                matrix[i][j], matrix[j][n-1-i], matrix[n-1-i][n-1-j], matrix[n-1-j][i] = \
                matrix[n-1-j][i], matrix[i][j], matrix[j][n-1-i], matrix[n-1-i][n-1-j]

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
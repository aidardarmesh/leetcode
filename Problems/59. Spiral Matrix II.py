from typing import *

class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        m = [[0 for j in range(n)] for i in range(n)]
        counter = 1

        for i in range(0, round(n/2)):
            for j in range(i, n-1-i):
                m[i][j] = counter
                counter += 1
        
            for j in range(i, n-1-i):
                m[j][n-1-i] = counter
                counter += 1
            
            for j in range(n-1-i, i, -1):
                m[n-1-i][j] = counter
                counter += 1
            
            for j in range(n-1-i, i, -1):
                m[j][i] = counter
                counter += 1

        if n % 2 == 1:
            m[n//2][n//2] = counter
        
        return m

s = Solution()

print(s.generateMatrix(4))